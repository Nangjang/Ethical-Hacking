#!/bin/python3

import sys
import socket
from datetime import datetime

if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1])
	
else:
	print("Invalid number of Arguments!")
	print("Syntax: python3 simpleportscanner.py <ip>")
	sys.exit()
	
print("*" * 50)
print("Scanning Ports:", target)
print("Starting Time:", datetime.now())
print("*" * 50)

try:
	for port in range(1, 85):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target, port))
		print("Checking Port:", port)
		if result == 0:
			print("Port {} is OPEN.".format(port))
		s.close()
		
except KeyboardInterrupt:
	print("\nProgram Terminated!")
	sys.exit()
	
except s.gaierror:
	print("\nHostname is not resolved!")
	sys.exit()
	
except s.error:
	print("\nCould not connect to the Server!")
	sys.exit()
