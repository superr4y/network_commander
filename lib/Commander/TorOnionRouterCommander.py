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


class TorOnionRouterCommander(TorBaseCommander):
    def __init__(self, **kwargs):
        '''
        doc doc doc
        '''
        # TODO: Search for a better way of doing that
        # 
        if 'nick_name' not in kwargs:
            kwargs['nick_name'] = 'or'
        super(TorOnionRouterCommander, self).__init__(
                        conf_tmpl='torrc.or.tmpl', **kwargs)

    def run(self, **kwargs):
        return self.exe.run_tor_or(**kwargs)
