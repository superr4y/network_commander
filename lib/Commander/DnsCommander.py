#!/usr/bin/env python3
import os, sys, shutil
#sys.path.append(os.path.abspath('../'))
from Environment.DnsEnvironment import DnsEnvironment
from Wrapper.Dns import Dns
import subprocess as sp

class DnsCommander:
    def __init__(self, *args, **kwargs):
        self.env = DnsEnvironment()
        self.exe = Dns(self.env)

    def configure(self):
        self._create_home_dir()
        self._create_conf_file()

    def run(self, **kwargs):
        return self.exe.run(**kwargs)

    def addDnsEntry(self, entry):
        with open(self.env.abs_conf_file(), 'a') as fd:
            fd.write(entry+'\n')

    def _create_home_dir(self):
        if not os.path.exists(self.env['home_dir']):
            os.makedirs(self.env['home_dir'])

    def _create_conf_file(self):
        with open(self.env.abs_conf_file(), 'w') as fd:
            fd.write('')
        
    def _destroy(self):
        shutil.rmtree(self.env['home_dir'])

    def __str__(self):
        return type(self).__name__
