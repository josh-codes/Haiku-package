import socket
async def send(broadcast, destip, bindip, eport, lport, data):
	"""Send UDP packets"""
	# Create socket
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
	except:
		return False
	if broadcast:
		# If target is a broadcast ip
		s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
	# Define variables
	lconfig = (bindip, lport)
	econfig = (destip, eport)
	sdata = data.encode("utf-8")
	# Bind local port
	s.bind(lconfig)
	# Send data
	s.sendto(sdata, econfig)
	# Close socket
	s.close()
	return True
