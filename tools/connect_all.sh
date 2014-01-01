#!/bin/bash

python2 log_packet_count_and_time.py 1&
proxychains phantomjs full_request.js http://10.0.0.3
kill -s SIGINT



