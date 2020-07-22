from IPget import get_ip
from UDPget import get
from UDPsend import send
async def getbright(fanip):
    result = False
    thisip = await get_ip()
    await send(False, fanip, thisip, 31415, 31415, "<ALL;LIGHT;LEVEL;GET;ACTUAL>")
    result = await get(5, thisip, 31415)
    if result is False:
        return
    bright = (result[0].split(";"))[4]
    bright = (bright.split(")"))[0]
    return bright*6.25
async def setbright(fanip, bright):
    rbright = round(bright/6.25)
    if rbright == 0:
        rbright = 1
    result = False
    thisip = await get_ip()
    data = "<ALL;LIGHT;LEVEL;SET;"+str(rbright)+">"
    await send(False, fanip, thisip, 31415, 31415, data)
    result = await get(5, thisip, 31415)
    if result is False:
        return
    ebright = (result[0].split(";"))[4]
    ebright = (bright.split(")"))[0]
    return ebright*6.25
async def setstate(fanip, state):
    result = False
    thisip = await get_ip()
    if state is True:
        nstate = 'ON'
    else:
        nstate = 'OFF'
    data = "<ALL;LIGHT;PWR;"+nstate+">"
    await send(False, fanip, thisip, 31415, 31415, data)
    result = await get(5, thisip, 31415)
    if result is False:
        return
    state = ((result[0]).split(";"))[3]
    state = (state.split(")"))[0]
    return state
