#!/usr/bin/env python3
from quik import FileLoader
import subprocess as sp
import quik
import os, sys, shutil
from itertools import chain
#sys.path.append(os.path.abspath('../'))
from Environment.TorEnvironment import TorEnvironment
from Commander.TorBaseCommander import TorBaseCommander
from Wrapper.Tor import Tor


class TorDirectoryAuthorityCommander(TorBaseCommander):
    def __init__(self, **kwargs):
        '''
        doc doc doc
        '''
        super(TorDirectoryAuthorityCommander, self).__init__(nick_name='da',
                        conf_tmpl='torrc.da.tmpl', **kwargs)

    def run(self, **kwargs):
        return self.exe.run_tor_da(**kwargs)
      

    def configure(self):
        super(TorDirectoryAuthorityCommander, self).configure()
        self.exe.gen_authority_key(stdin=sp.PIPE).communicate(b'password\n')
        #self.exe.gen_authority_key(stdin=sp.PIPE).communicate(b'password')
        self.exe.gen_fingerprint(stdin=sp.PIPE).communicate(b'\n')

