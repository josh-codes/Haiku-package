import asyncio
sdata=""
addr=""
class udpProto:
	def connection_made(self, transport):
		self.transport = transport
		senddata = sdata.encode('utf8')
		self.transport.sendto(senddata, addr)
		transport.close()

	def datagram_received(self, data, addr):
		# I have to do something here
		something = True

async def send(broadcast, destip, bindip, eport, lport, data):
	loop = asyncio.get_running_loop()
	global sdata
	sdata = data
	global addr
	addr = (destip, eport)
	transport, protocol = await loop.create_datagram_endpoint(
		lambda: udpProto(),
		local_addr=(bindip, lport))

	try:
		await asyncio.sleep(6)
	finally:
		return True
