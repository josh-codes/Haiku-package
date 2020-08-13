import asyncio
class udpProto:
	def __init__(self, sdata, addr, on_done):
		self.sdata = sdata
		self.addr = addr
		self.on_done = on_done
		self.transport = None

	def connection_made(self, transport):
		self.transport = transport
		senddata = (self.sdata).encode('utf8')
		self.transport.sendto(senddata, self.addr)
		transport.close()
		self.on_done.set_result(True)

	def datagram_received(self, data, addr):
		# I have to do something here
		something = True

	def connection_lost(self, stuff):
		# I have to do something here
		something = True

async def send(broadcast, destip, bindip, eport, lport, data):
	loop = asyncio.get_running_loop()
	on_done = loop.create_future()
	sdata = data
	addr = (destip, eport)
	transport, protocol = await loop.create_datagram_endpoint(
		lambda: udpProto(sdata, addr, on_done),
		local_addr=(bindip, lport),
		allow_broadcast=True)

	try:
		await on_done
	finally:
		return True
