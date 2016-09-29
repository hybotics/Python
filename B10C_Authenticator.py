#!/usr/bin/env python3
import requests
import json

class B10C_Authenticator:
	urlbase = "https://api.10centuries.org/auth/login"
	app_id = "YOUR APP ID"

	def __init__ (self, username, userpass):
		acct_data = {
			"client_guid" :  self.app_id,
			"acctname" :  username,
			"acctpass" :  userpass
		}

		result = requests.post(self.urlbase, data=acct_data)

		self.result = result

		print ("library: result = '{0}'".format(result))

		return None