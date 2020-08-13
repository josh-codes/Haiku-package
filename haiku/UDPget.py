import asyncio
msg=""
ip = ""
class udpProto:
    def connection_made(self, transport):
        self.transport = transport

    def datagram_received(self, data, addr):
        msg = data.decode()
        ip = addr
        transport.close()


async def get(timeout, bindip, revport):
    loop = asyncio.get_running_loop()
    transport, protocol = await loop.create_datagram_endpoint(
        lambda: udpProto(),
        local_addr = (bindip, revport))

    try:
        await asyncio.sleep(timeout)
    finally:
    	if addr == "": 
        	transport.close()
        	ret = False
        return [msg,ip]
