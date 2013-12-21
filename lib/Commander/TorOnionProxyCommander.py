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


class TorOnionProxyCommander(TorBaseCommander):
    def __init__(self, **kwargs):
        '''
        doc doc doc
        '''
        super(TorOnionProxyCommander, self).__init__(nick_name='op',
                        conf_tmpl='torrc.op.tmpl', **kwargs)

    def run(self, **kwargs):
        return self.exe.run_tor_op(**kwargs)
