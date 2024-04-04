"""
Author: Aleksa Zatezalo
Name: Create RCE on servers running ManageEngine Applications
Description: A python script made to test for potential sqli attacks.
Version: 1.0
"""

import argparse
import socketserver
import threading

def testSQLi(url, payload):
    """
    """
    pass

def testPrivelege(url, payload):
    """
    """
    pass

def revShellUpload(url):
    """
    """
    pass

def revShellExec(url):
    """
    """
    pass

def getShellWindows(url, lhost, lport):
    """
    Gets a shell on target system, url, running managed engine.
    Offers CLI on ip address, lhost, and port, lport. 
    This exploit is specific to Windows.
    """
    pass

def getShell(url, lhost, lport):
    """
    Gets a shell on target system, url, running managed engine.
    Offers CLI on ip address, lhost, and port, lport.
    This exploit works on all systems.
    """
    pass

def execute(cmd):
    """
    """
    pass

def main():
    """
    """
    # parser = argparse.ArgumentParser(description='BHP Net Tool', formatter_class=argparse.RawDescriptionHelpFormatter,
    #                                  epilog=textwrap.dedent('''Example:\nnetcat.py -t 192.168.1.108 - p 555 -l -c #command shell
    #                                  netcat.py -t 192.168.1.108 - p 555 -l -u=mytest.txt #file to upload
    #                                  netcat.py -t 192.168.1.108 - p 555 -l -e \"cat /etc/passwd\" #execute command
    #                                  echo ABC | ./netcat.py -t 192.168.1.108 - p 135 #echo text to port 135
    #                                  netcat.py -t 192.168.1.108 - p 555 #connect to server'''))
    # parser.add_argument('-c', '--command', action='store_true', help='command shell')
    # parser.add_argument('-e', '--execute', help='execute specific command')
    # parser.add_argument('-l', '--listen', action='store_true', help='listen')
    # parser.add_argument('-p', '--port', type=int, default=5555, help='specified port')
    # parser.add_argument('-t', '--target', default='192.168.1.203', help="specific IP")
    # parser.add_argument('-u', '--upload', help='upload file')
    # args = parser.parse_args()
    pass

if __name__ == '__main__':
    pass