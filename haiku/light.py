from haiku import IPget
from haiku import UDPget
from haiku import UDPsend
async def getbright(fanip):
    result = False
    thisip = await IPget.get_ip()
    await UDPsend.send(False, fanip, thisip, 31415, 31415, "<ALL;LIGHT;LEVEL;GET;ACTUAL>")
    result = await UDPget.get(5, thisip, 31415)
    if result is False:
        return
    bright = (result[0].split(";"))[4]
    bright = (bright.split(")"))[0]
    return round(int(bright)*6.25)
async def setbright(fanip, bright):
    rbright = round(bright/6.25)
    if rbright == 0:
        rbright = 1
    result = False
    thisip = await IPget.get_ip()
    data = "<ALL;LIGHT;LEVEL;SET;"+str(rbright)+">"
    await UDPsend.send(False, fanip, thisip, 31415, 31415, data)
    result = await UDPget.get(5, thisip, 31415)
    if result is False:
        return
    ebright = (result[0].split(";"))[4]
    ebright = (bright.split(")"))[0]
    return round(int(ebright)*6.25)
async def setstate(fanip, state):
    result = False
    thisip = await IPget.get_ip()
    if state is True:
        nstate = 'ON'
    else:
        nstate = 'OFF'
    data = "<ALL;LIGHT;PWR;"+nstate+">"
    await UDPsend.send(False, fanip, thisip, 31415, 31415, data)
    result = await UDPget.get(5, thisip, 31415)
    if result is False:
        return
    state = ((result[0]).split(";"))[3]
    state = (state.split(")"))[0]
    return state
