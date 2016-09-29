#!/usr/bin/env python3

from B10C_Authenticator import B10C_Authenticator

u_name = "YOUR USER ID"
u_pass = "YOUR PASSWORD"

code = ""
error = ""
token = ""

# Authenticate the user account with 10Centuries
b10c = B10C_Authenticator(u_name, u_pass)

print ("application: b10c.result = '{0}'".format(b10c.result))
'''
code = a10c.code

if code == "200":
	print ("Login was successful!")
	token = a10c.token
else:
	print ("Login failed - error = %s", a10c.error)
'''
