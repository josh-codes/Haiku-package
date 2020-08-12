import asyncio
import concurrent.futures
mssg=""
ip = ""
class udpProto:
    def connection_made(self, transport):
        self.transport = transport

    def datagram_received(self, data, addr):
        msg = data.decode()
        ip = addr
        transport.close()


async def get_send(timeout, bindip, revport):
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
        else:
        	paddr = ("\'"+addr+"\'", bindip)
        return [data,paddr]

async def get(timeout, bindip, revport):
	with concurrent.futures.ThreadPoolExecutor() as executor:
	    future = executor.submit(await get_send, (timeout, bindip, revport))
	    result = future.result()
	    return result
