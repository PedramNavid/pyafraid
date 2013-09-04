import codecs
import socket
import re
import urllib.request
import configparser
import os
import sys

def get_config(fname):
    config = configparser.ConfigParser()
    config['Settings'] = { 'apikey': 'YOURAPIKEY',
                          'domain': 'YOURDOMAIN.afraid.org'}
    if not os.path.exists(fname):
        with open(fname, 'w') as configfile:
            config.write(configfile)
    config.read(fname)
    return config

def get_ip():
    url = 'http://whatsmyip.net'
    result = codecs.decode(urllib.request.urlopen(url).read())
    ip = re.findall('<input type="text" value="([0-9.]+)', result)[0]
    return ip

def get_registered(domain):
    return socket.gethostbyname(domain)

def register(ip, domain, apikey):
    if get_registered(domain) != ip:
        updateurl = 'http://freedns.afraid.org/dynamic/update.php?'
        url = updateurl + apikey
        result = codecs.decode(urllib.request.urlopen(url).read())
        return result
    else:
        return "IP {} hasn't changed, nothing done.".format(ip)

if __name__ == '__main__':
    config = get_config('afraid.rc')
    if config['Settings']['apikey']=='YOURAPIKEY':
        print('Config not set. Please enter your api key and domain in the afraid.rc file')
        sys.exit(1)
    apikey = config['Settings']['apikey']
    domain = config['Settings']['domain']
    print(register(get_ip(), domain, apikey))
