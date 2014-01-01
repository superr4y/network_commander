#!/usr/bin/env python2

from scapy.sendrecv import sniff
from scapy.layers.inet import ICMP, IP
from time import time
import signal
import subprocess as sp
import sys


pkg = []
all_pkg = []
file_name = sys.argv[1]


def dump(packet):
    pkg.append({'payload': len(packet.payload), 'time': time(),
                'sport': packet.sport, 'dport': packet.dport,
                'src': packet.payload.src, 'dst': packet.payload.dst})
    #print(pkg[-1][-1])

def alarm_handler(*args):
    global pkg
    print('[+] Next Request')
    all_pkg.append(pkg)
    # for some reason finally does not execute (main loop)
    # just to get the data out
    with open(file_name, 'w') as fd:
        fd.write(str(all_pkg))
    pkg = []

signal.signal(signal.SIGALRM, alarm_handler)

while True:
    try:
        sniff(iface='eth10', filter='tcp', prn=dump)
    except KeyboardInterrupt:
        print('[+] sigint')
        break
    finally:
        print('[+] write dump to file => {0}'.format(file_name))
        with open(file_name, 'w') as fd:
            fd.write(str(all_pkg))
        
print('[+] The Ende')


'''
def part_pkg(pkg):
    part = {}
    for p in pkg:
        key = '{0} -> {1}'.format(p['sport'], p['dport'])
        if key not in part.keys():
            part[key] = []
        part[key].append(p)
    return part

def distance_function(pkg):
    x_list, y_list = [], []
    for request in pkg:
        x, y = (request[-1]['time'] - request[0]['time'])*100, 0
        for packet in request:
            y += int(packet['payload'])
        x_list.append(x)
        y_list.append(y)
    return (x_list, y_list)
'''
