import asyncio
class udpProto:
	def __init__(self, on_done, msg, ip):
		self.msg = msg
		self.ip = ip
		self.on_done = on_done
		self.transport = None
		self.msg.set_result("")
		self.ip.set_result("")
		self.on_done.set_result(False)

	def connection_made(self, transport):
		self.transport = transport

	def datagram_received(self, data, addr):
		transport.close()
		self.msg.set_result(data.decode())
		self.ip.set_result(addr)
		self.on_done.set_result(True)

	def connection_lost(self, stuff):
		# I have to do something here
		something = True

async def get(timeout, bindip, revport):
	loop = asyncio.get_running_loop()
	on_done = loop.create_future()
	msg = loop.create_future()
	ip = loop.create_future()
	time = timeout/10
	transport, protocol = await loop.create_datagram_endpoint(
		lambda: udpProto(on_done, msg, ip),
		local_addr = (bindip, revport))

	try:
		for i in range(10):
			ondoneres = str(on_done).split('=')
			ondoneres = (ondoneres[1]).split('>')
			ondoneres = ondoneres[0]
			if ondoneres == 'False':
				await asyncio.sleep(time)
	finally:
		if str(ip) == "<Future finished result=\'\'>": 
			transport.close()
			ret = False
		else:
			ret = [msg,ip]
	return ret
