#!/usr/bin/env python
import subprocess as sp
import signal
import time

l = sp.Popen('python2 dump_data.py {0}'.format('/tmp/test3/data.txt'), shell=True)

for r in range(1, 5): # do the test 4 times
    for index in range(1,5): # all websites
        out = sp.Popen('proxychains phantomjs full_request.js http://10.0.0.{0}'.format(index+2), shell=True, stdout=sp.PIPE)
        out.wait()
        time.sleep(5)  # just for testing
        l.send_signal(signal.SIGALRM)

'''
print('[+] create image with distances')

# This is bad but I don't care for now
with open('/tmp/test3/packets.txt', 'r') as fd:
    packets = fd.read()
pkg = eval(packets)
x_list, y_list = distance_function(pkg)
print(x_list, y_list)
#for x, y, i in zip(x_list, y_list, range(len(x_list))):
#    text(x+5, y+5, '10.0.0.{0}'.format(i+3))
scatter(x_list, y_list)
savefig('/tmp/test3/diff3.png')
'''
