"""
Author: Aleksa Zatezalo.
Date: September 2024.
Title: Managed Engine RCE.
Description: An RCE for the Manged Engine Web Application via SQL.
"""

import requests
from colorama import Fore, Back, Style

def format_text(title, item):
    cr = '\r\n'
    section_break = cr + "*" * 20 + cr
    item = str(item)
    text = Style.BRIGHT + Fore.RED + title + Fore.RESET + section_break + item + section_break
    return text 

proxies = {'http':'http://127.0.0.1:8080','https':'http://127.0.0.1:8080'}

r = requests.get('https://manageengine:8443/', verify=False, proxies=proxies)
print(format_text('r.status_code is:', r.status_code))
print(format_text('r,headers is: ', r.headers))
print(format_text('r.cookies is: ', r.cookies))
print(format_text('r.text is: ', r.text))