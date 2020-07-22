from IPget import get_ip
from UDPget import get
from UDPsend import send
import time
async def discover(hstr):
    thisip = await get_ip()
    if thisip is False:
        return False
    iplist = thisip.split(".")
    iplist.pop()
    iplist.append("255")
    broadip = ".".join(iplist)
    await send(True, broadip, thisip, 31415, 31415, "<ALL;DEVICE;ID;GET>")
    timeend = time.time() + 5
    jumfanip = None
    while time.time() < timeend:
        result = await get(0.01, thisip, 31415)
        if result is not False:
            if result[0] == hstr:
                jumfanip = result[1]
                jumfanip = jumfanip[0]
                return jumfanip
    if jumfanip is None:
        return
