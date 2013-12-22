#!/usr/bin/env python3
from .Wrapper import ExecuteOrNot, Debug

class Http:
    def __init__(self, env):
        """
        """
        self.env = env

    
    @ExecuteOrNot   
    def run(self, **kwargs):
        cmd = 'su -c "lighttpd -f {0}"'.format(self.env.abs_conf_file())
        print(cmd)
        return cmd
