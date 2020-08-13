import asyncio
sdata=""
addr=""
e = ""
class udpProto:
	def connection_made(self, transport):
		global e
		self.transport = transport
		senddata = sdata.encode('utf8')
		self.transport.sendto(senddata, addr)
		transport.close()
		e = True

	def datagram_received(self, data, addr):
		# I have to do something here
		something = True
	def connection_lost(self, stuff):
		e = True

async def send(broadcast, destip, bindip, eport, lport, data):
	loop = asyncio.get_running_loop()
	global sdata
	sdata = data
	global addr
	addr = (destip, eport)
	transport, protocol = await loop.create_datagram_endpoint(
		lambda: udpProto(),
		local_addr=(bindip, lport),
		allow_broadcast=True)

	try:
		while e is not True:
			await asyncio.sleep(0.1)
	finally:
		return True
