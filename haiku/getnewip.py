from haiku import IPget
from haiku import UDPget
from haiku import UDPsend
import time
async def discover(hstr):
    thisip = await IPget.get_ip()
    if thisip is False:
        return False
    iplist = thisip.split(".")
    iplist.pop()
    iplist.append("255")
    broadip = ".".join(iplist)
    await UDPsend.send(True, broadip, thisip, 31415, 31415, "<ALL;DEVICE;ID;GET>")
    timeend = time.time() + 5
    jumfanip = None
    while time.time() < timeend:
        result = await UDPget.get(0.01, thisip, 31415)
        if result is not False:
            if result[0] == hstr:
                jumfanip = result[1]
                jumfanip = jumfanip[0]
                return jumfanip
    if jumfanip is None:
        return
