from haiku import IPget
from haiku import UDPget
from haiku import UDPsend
import time
async def discover():
    thisip = await IPget.get_ip()
    if thisip is False:
        return False
    iplist = thisip.split(".")
    iplist.pop()
    iplist.append("255")
    broadip = ".".join(iplist)
    await UDPsend.send(True, broadip, thisip, 31415, 31415, "<ALL;DEVICE;ID;GET>")
    timeend = time.time() + 5
    devicelist = []
    lightlist = []
    fanlist = []
    reuse = False
    while time.time() < timeend:
        result = await UDPget.get(0.01, thisip, 31415)
        if reuse is False:
        	reuse = True
        if result is not False and result not in devicelist:
            devicelist.append(result)
    for getinfo in range (len(devicelist)):
        jumfanip = (devicelist[getinfo])[1]
        jumfanip = str(jumfanip).split("\'")
        fanip = jumfanip[1]
        await UDPsend.send(False, fanip, thisip, 31415, 31415, "<ALL;DEVICE;LIGHT;GET>")
        result = await UDPget.get(5, thisip, 31415)
        light = None
        if result is not False:
            light = str(result).split(",")
            light = (light[0]).split("\'")
            light = (light[1]).split("(")
            light = (light[1]).split(")")
            light = (light[0]).split(";")
            if len(light) == 3:
                return
            if light[3] == "PRESENT":
                light = True
            else:
                light = False
        else:
            return
        if light is None:
            return
        faninfo = (devicelist[getinfo])[0]
        faninfo = (faninfo.split(")"))[0]
        faninfo = (faninfo.split("("))[1]
        faninfo = faninfo.split(";")
        fanname = faninfo[0]
        fanmac = faninfo[3]
        fanstr = (devicelist[getinfo])[0]
        fanuid = "("+str(fanmac)+";fan)"
        fancip = fanip
        fanlist.append([fanname, fanstr, fanuid, fancip])
        if light is True:
            lightuid = "("+str(fanmac)+";light)"
            lightlist.append([fanname, fanstr, lightuid, fancip])
        getinfo += 1
    return[lightlist, fanlist]
