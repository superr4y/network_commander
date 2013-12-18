#!/usr/bin/env python3
import subprocess as sp
import re, time

import sys, os
sys.path.append(os.path.abspath('../'))
from Wrapper.Wrapper import ExecuteOrNot, Debug

LXC_PATH='/usr/bin/'


class LxcIsAlreadRunningException(Exception):
    def __init__(self, *args):
        #super.__init__(args)
        pass
class LxcConfException(Exception):
    def __init__(self):
        pass


class Lxc:
    def __init__(self, config_file):
        self.config_file = config_file

    @ExecuteOrNot
    def execute(self, command, **kwargs):
        if self._is_running():
            raise LxcIsAlreadRunningException()

        #cmd = [LXC_PATH+'lxc-execute', '-n', self._lxc_name(), '-f', self.config_file,
        #       '--'] + command
        cmd = '{0}lxc-execute -n {1} -f {2} -- {3}'.format(
            LXC_PATH, self._lxc_name(), self.config_file, command)
        return cmd
                    
    @ExecuteOrNot
    def attach(self, **kwargs):
        #cmd = [LXC_PATH+'lxc-attach', '-n', self._lxc_name()]
        cmd = '{}lxc-attach -n {1}'.format(LXC_PATH, self._lxc_name())
        return cmd
    
    @ExecuteOrNot
    def stop(self, **kwargs):
        #cmd = [LXC_PATH+'lxc-stop', '-n', self._lxc_name()]
        cmd = '{0}lxc-stop -n {1}'.format(LXC_PATH, self._lxc_name())
        return cmd

    def _is_running(self):
        """
        Checks the output from lxc-info if RUNNING is included
        """
        cmd = [LXC_PATH+'lxc-info', '-n', self._lxc_name()]
        for _ in range(10): # just to be sure repeate it 10 times
            time.sleep(0.1)
            output = sp.check_output(cmd)
            match = re.search(r'state:\s+(\S+)', output.decode(encoding='utf-8'))
            state = match.group(1)
            if state == 'RUNNING':
                return True
        return state == 'RUNNING'
            

    def _lxc_name(self):
        """
        Parse config_file for lxc.utsname = name
        and retruns name

        >>> Lxc('../../test/lxc.conf')._lxc_name()
        'vm0'
        """

        with open(self.config_file, 'r') as fd:
            conf = fd.read()
        
        match = re.search(r'lxc.utsname\s+=\s+(\S+)', conf)
        if(not match):
            raise LxcConfException()
        return match.group(1)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    lxc = Lxc('../../test/lxc.conf')
    print(lxc.execute(['nc', '-lnvp', '6666'], no_exec=False))
    print(lxc._is_running())
    print(lxc.stop())
    print(lxc._is_running())
            
            
            
            
            
        

