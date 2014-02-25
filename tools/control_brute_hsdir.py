#!/usr/bin/env python3
from stem.control import Controller
import sys

with Controller.from_port(port=9051) as controller:
    controller.authenticate()
    msg = 'BRUTEHSDIR 1 {0} {1} {2}'.format(sys.argv[1], sys.argv[2], sys.argv[3])
    print(msg)
    resp = controller.msg(msg)
    
    #print(resp)
