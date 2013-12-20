#!/usr/bin/env python3
from quik import FileLoader
import subprocess as sp
import quik
import os, sys, shutil
from itertools import chain
#sys.path.append(os.path.abspath('../'))
from Environment.TorEnvironment import TorEnvironment
from Wrapper.Tor import Tor


class TorDirectoryAuthorityCommander:
    def __init__(self):
        '''
        doc doc doc
        '''
        self.env = TorEnvironment(nick_name='da')
        self.exe = Tor(self.env)
   

    def run(self, **kwargs):
        return self.exe.run_tor_da(**kwargs)
      
    ##### TODO: is this so generic that i could create a Commander class??? #####
    def configure(self):
        self._create_home_dir()
        self._create_conf_file()

    def _create_home_dir(self):
        if not os.path.exists(self.env['home_dir']):
            os.makedirs(self.env['home_dir'])

    def _create_conf_file(self):
        loader  = FileLoader('/')
        template = loader.load_template(self.env.abs_conf_tmpl())
        conf = template.render(self.env)
        with open(self.env.abs_conf_file(), 'w') as fd:
            fd.write(conf)
    ##### TODO: is this so generic that i could create a Commander class??? #####



    def update_new_tor_da(self, da_env):
        # This should be in TorCommanderBase
        entry = da_env.torrc_da_entry()
        with open(self.env.abs_conf_file(), 'a') as fd:
            fd.write('\n{0}\n'.format(entry))

