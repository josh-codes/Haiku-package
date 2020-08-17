import asyncio
class udpProto:
	msg = ""
	ip = ""
	def __init__(self, on_done):
		self.on_done = on_done
		self.transport = None
		self.msg = ""
		self.ip = ""

	def connection_made(self, transport):
		self.transport = transport

	def datagram_received(self, data, addr):
		self.transport.close()
		self.msg = (data.decode())
		self.ip = (addr)
		self.on_done.set_result(True)

	def connection_lost(self, stuff):
		# I have to do something here
		something = True

async def get(timeout, bindip, revport):
	loop = asyncio.get_running_loop()
	on_done = loop.create_future()
	classcmd = udpProto(on_done)
	time = timeout/10
	transport, protocol = await loop.create_datagram_endpoint(
		lambda: classcmd,
		local_addr = (bindip, revport),
		reuse_port = True)

	try:
		for i in range(10):
			ondoneres = str(on_done).split('=')
			if str(on_done) == '<Future pending>':
				await asyncio.sleep(time)
	finally:
		if classcmd.ip == "": 
			transport.close()
			ret = False
		else:
			ret = [classcmd.msg,classcmd.ip]
	return ret
