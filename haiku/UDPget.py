import socket
import concurrent.futures
async def get_send(timeout, bindip, revport):
	"""Get UDP packets"""
	# Create socket
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
	except:
		return False
	# Set timeout
	s.settimeout(timeout)
	# Define variables
	econfig = (bindip, revport)
	# Bind receiving port
	s.bind(econfig) 
	# Try to get data
	try:
		data, address = s.recvfrom(4096)
	except:
		return False
	dedata = data.decode("utf-8")
	return [dedata, address]

async def get(timeout, bindip, revport):
	with concurrent.futures.ThreadPoolExecutor() as executor:
	    future = executor.submit(await get_send, timeout, bindip, revport)
	    result = future.result()
	    return result
