#------------------------------------------------------
#      BY: UNDEADSEC from BRAZIL :)
#      YouTube: https://www.youtube.com/c/UndeadSec
#      Github: https://github.com/UndeadSec/IP-NET
#------------------------------------------------------
from ipaddress import ip_network, ip_address
from os import listdir

RED, WHITE, GREEN, END, YELLOW = '\033[91m', '\33[97m', '\033[1;32m', '\033[0m', '\33[93m'

def readFile(filepath):
    f = open(filepath, 'r')
    return f.read()

def getIps():
    iplist = []
    files = listdir('ips/')
    for f in files:
        ips = readFile('ips/' + f).split('\n')
        for ip in ips:
            iplist.append(ip)
    return iplist

def getRanges():
    rangelist = []
    files = listdir('ranges/')
    for f in files:
        rgs = readFile('ranges/' + f).split('\n')
        for rang in rgs:
            rangelist.append(rang)
    return rangelist

iplist = getIps()
rangelist = getRanges()

print(f'''
  _____ _____ {RED}___{END}  _   _ ______ _______ 
 |_   _|  __ \{RED}__ \{END}| \ | |  ____|__   __|
   | | | |__) |{RED} ){END} |  \| | |__     | |   
   | | |  ___/ {RED}/ /{END}| . ` |  __|    | |   
  _| |_| |    {RED}|_|{END} | |\  | |____   | |   
 |_____|_|    {RED}(_){END} |_| \_|______|  |_|   
                                        
 Check if IPs matches networks - @{RED}UndeadSec{END}''')

for rang in rangelist:
    net = ip_network(rang)
    print(f' \n#{YELLOW}###{END}# Checking network: {YELLOW}{rang}{END}')
    for ip in iplist:
        try:
            if ip_address(ip) in net:
                print(f'\n {GREEN}[{END}*{GREEN}]{END} Match found: {GREEN}{ip}{END} - {GREEN}{rang}{END}')
            else:
                pass
        except Exception as e:
            print(e)