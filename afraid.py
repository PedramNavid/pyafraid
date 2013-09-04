import urllib2
import re
import socket


def get_ip():
    url = 'http://whatsmyip.net'
    result = urllib2.urlopen(url).read()
    ip = re.findall('<input type="text" value="([0-9.]+)', result)[0]
    return ip

def get_registered(domain):
    return socket.gethostbyname(domain)

def register(ip, domain, apikey):
    if get_registered(domain) != ip:
        updateurl = 'http://freedns.afraid.org/dynamic/update.php?'
        url = updateurl + apikey
        result = urllib2.urlopen(url).read()
        return result

if __name__ == '__main__':
    apikey='Nkg1OHBqdW9QSkxSdGlINVhXNEo6ODUxMzI3OQ=='
    domain = 'multiphrenic.mooo.com'
    register(get_ip(), domain, apikey)
