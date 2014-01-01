#!/usr/bin/env python2

from scapy.sendrecv import sniff
from scapy.layers.inet import ICMP, IP
from time import time
import subprocess as sp
import sys

from pylab import *

pkg = []
index = sys.argv[1]

colors = ['blue', 'red', 'yellow', 'green', 'black']

def dump(packet):
    pkg.append({'payload': len(packet.payload), 'time': time(),
                'sport': packet.sport, 'dport': packet.dport,
                'src': packet.payload.src, 'dst': packet.payload.dst})
    print(pkg[-1])

def part_pkg(pkg):
    part = {}
    for p in pkg:
        key = '{0} -> {1}'.format(p['sport'], p['dport'])
        if key not in part.keys():
            part[key] = []
        part[key].append(p)
    return part

def calc_x(pkg):
    return [ abs(pkg[0]['time'] - p['time'])*100 for p in pkg]

def calc_y(pkg):
    return [p['payload'] for p in pkg]

try:
    sniff(iface='eth10', filter='tcp', prn=dump)
except KeyboardInterrupt:
    pass




text(-5.0, -5.0, 'http://10.0.0.{0}'.format(int(index)+2), fontsize=12)
part = part_pkg(pkg)
legend_list = []
for k, c in zip(part.keys(), colors):
    x, y = calc_x(part[k]), calc_y(part[k])
    print('#'*10, k, c, '#'*10)
    points = scatter(x, y, c=c)
    legend_list.append({'points': points, 'key': k})
legend( [e['points'] for e in legend_list], [e['key'] for e in legend_list] ) 
savefig('/tmp/test/fig_{0}.png'.format(index))

#sp.Popen('display /tmp/fig_{0}.png'.format(index), shell=True)












