#!/usr/bin/python3

"""
Author: Aleksa Zatezalo
Name: Recon.
Description: A python library created to help enumerate web applicaitons.
Version: 1.0
"""

import requests
import urllib3
from colorama import Fore, Back, Style

requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

def format_text(title, item):
    """
    Formats http responses with a title , title, and http content, item.
    Returns a constructed string, text, that is a human readble HTTP response.

    String: title - the title of an http variable (foe example r.headers).
    String: item - the http information to be returned.
    Return: a formated string composed of title and item.
    """
    cr = '\r\n'
    section_break = cr + "*" * 20 +  cr

    item = str(item)
    text = Style.BRIGHT + Fore.RED + title + Fore.RESET + section_break + item + section_break
    return text

def basic_get_request(url, proxy=None):
    """
    Performs a basic get request with no arguments to address url. Prints http(s) response
    to standard output. This function has no returns.

    String: url - the url of site you intend to perform a get resqust on. 
    Proxies: a dictionary containing two keys (http, https) and the corrisponding proxy values.
    """

    if (proxy != None):
        r = requests.get(url, verify=False, proxies=proxy)
    else:
        r = requests.get(url,verify=False)
    
    
    print(format_text('r.status_code is: ',r.status_code))
    print(format_text('r.headers is: ',r.headers))
    print(format_text('r.cookies is: ',r.cookies))
    print(format_text('r.text is: ',r.text))
    
    return 0

def test_sqli(url, pay):
    """
    Formats a URL, url, to contains a payload, pay. Sends the corresponding HTTP request.
    """
    
    r = requests.get(url, params=pay, verify=False)
    print(format_text('r.headers is: ',r.headers))
    print(format_text('r.text is: ',r.text))