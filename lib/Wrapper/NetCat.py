#!/usr/bin/env python3
import subprocess as sp

import sys, os
sys.path.append(os.path.abspath('../'))
from Wrapper.Wrapper import ExecuteOrNot, Debug

class NetCat:
    def __init__(self):
        """This is just a simple test wrapper class

        """
        pass

    
    @ExecuteOrNot   
    def listen(self, port, **kwargs):
        #cmd = ['nc', '-lnvp', str(port)]
        cmd = 'nc -lnvp {0}'.format(port)
        return cmd
        #sp.check_call(cmd)

    @ExecuteOrNot
    def connect(self, host, port):
        cmd = ['nc', host, str(port)]
        return cmd

if __name__ == '__main__':
    nc = NetCat()
    print(nc.listen(6666, execute=True, shell=True).communicate())
    from subprocess import Popen
    Popen('killall nc', shell=True)

