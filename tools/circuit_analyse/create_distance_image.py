#!/usr/bin/env python2

import sys
from pylab import *

file_name = sys.argv[1]
colors = ['blue', 'red', 'yellow', 'green', 'black']


def part_pkg(pkg):
    part = {}
    for p in pkg:
        key = '{0} -> {1}'.format(p['sport'], p['dport'])
        if key not in part.keys():
            part[key] = []
        part[key].append(p)
    return part

def distance_function(all_pkg):
    x_list, y_list = [], []
    for request in all_pkg:
        if len(request) < 2:
            continue
        x, y = (request[-1]['time'] - request[0]['time'])*100, 0
        for packet in request:
            y += int(packet['payload'])
        x_list.append(x)
        y_list.append(y)
    return (x_list, y_list)



print('[+] load network data from => {0}'.format(file_name))
with open(file_name, 'r') as fd:
    data = fd.read()
all_pkg = eval(data)



print('[+] create image with distances')

x_list, y_list = distance_function(all_pkg)
    #for x, y, i in zip(x_list, y_list, range(len(x_list))):
    #    text(x+5, y+5, '10.0.0.{0}'.format(i+3))
scatter(x_list, y_list)
savefig('/tmp/test3/diff.png')


