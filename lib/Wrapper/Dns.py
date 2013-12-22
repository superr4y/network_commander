#!/usr/bin/env python3
import subprocess as sp

#import sys, os
#sys.path.append(os.path.abspath('../'))
from .Wrapper import ExecuteOrNot, Debug

class Dns:
    def __init__(self, env):
        """
        """
        self.env = env

    
    @ExecuteOrNot   
    def run(self, **kwargs):
        cmd = 'su -c "{0} {1}"'.format(self.env['dns_bin'], self.env.abs_conf_file())
        print(cmd)
        return cmd
