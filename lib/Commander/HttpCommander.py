#!/usr/bin/env python3
from quik import FileLoader
import quik
import os, sys, shutil
#sys.path.append(os.path.abspath('../'))
from Environment.HttpEnvironment import HttpEnvironment
from Wrapper.Http import Http
import subprocess as sp

class HttpCommander:
    def __init__(self, *args, **kwargs):
        self.env = HttpEnvironment(**kwargs)
        self.exe = Http(self.env)

    def configure(self):
        self._create_home_dir()
        self._create_conf_file()

    def run(self, **kwargs):
        return self.exe.run(stdout=sp.PIPE, stderr=sp.STDOUT, **kwargs)

    def _create_home_dir(self):
        if not os.path.exists(self.env['home_dir']):
            os.makedirs(self.env['home_dir'])

        if 'symlink' not in self.env:
            os.makedirs(os.path.join(self.env['home_dir'], 'www'))
        else:
            os.symlink(self.env['symlink'], os.path.join(self.env['home_dir'], 'www'))

    def _create_conf_file(self):
        loader  = FileLoader('/')
        template = loader.load_template(self.env.abs_conf_tmpl())
        nc_conf = template.render(self.env)
        with open(self.env.abs_conf_file(), 'w') as fd:
            fd.write(nc_conf)
        
    def _destroy(self):
        shutil.rmtree(self.env['home_dir'])

    def __str__(self):
        return type(self).__name__
