from IPget import get_ip
from UDPget import get
from UDPsend import send
async def getspeed(fanip):
    result = False
    thisip = await get_ip()
    await send(False, fanip, thisip, 31415, 31415, "<ALL;FAN;SPD;GET;ACTUAL>")
    result = await get(5, thisip, 31415)
    if result is False:
        return
    speed = (result[0].split(";"))[4]
    speed = (speed.split(")"))[0]
    return speed
async def setspeed(fanip, speed):
    if speed == 0:
        speed = 1
    result = False
    thisip = await get_ip()
    data = "<ALL;FAN;SPD;SET;"+str(speed)+">"
    await send(False, fanip, thisip, 31415, 31415, data)
    result = await get(5, thisip, 31415)
    if result is False:
        return
    speed = (result[0].split(";"))[4]
    speed = (speed.split(")"))[0]
    return speed
async def setstate(fanip, state):
    result = False
    thisip = await get_ip()
    if state is True:
        nstate = 'ON'
    else:
        nstate = 'OFF'
    data = "<ALL;FAN;PWR;"+nstate+">"
    await send(False, fanip, thisip, 31415, 31415, data)
    result = await get(5, thisip, 31415)
    if result is False:
        return
    state = ((result[0]).split(";"))[3]
    state = (state.split(")"))[0]
    return state
