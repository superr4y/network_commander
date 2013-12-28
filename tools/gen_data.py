#!/usr/bin/env python3
'''
This script is used for generating traffic in the Tor network.
Please edit the urls to fit your needs.
'''

import random, time
import subprocess as sp

urls = ['http://10.0.0.3', 'http://10.0.0.4', 'http://10.0.0.5', 'http://10.0.0.6']

while True:
    url = urls[random.randint(0, len(urls)-1)]
    stdout, stdin = sp.Popen('proxychains phantomjs full_request.js {0}'.format(url),
                             shell=True, stdout=sp.PIPE).communicate()
    print(stdout)
    time.sleep(random.randint(3, 10))
