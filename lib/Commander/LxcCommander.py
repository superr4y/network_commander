#!/usr/bin/env python3
from quik import FileLoader
import subprocess as sp
import quik
import os, sys, shutil
sys.path.append(os.path.abspath('../'))
from Environment.LxcEnvironment import LxcEnvironment
from Wrapper.Lxc import Lxc


class LxcCommander:
    def __init__(self, commanders, *args, **kwargs):
        self.env = LxcEnvironment()
        self.exe = Lxc(self.env.conf_file())
        self.commanders = commanders

        # e.g. /tmp/net/netcat0 => /home/net/lxc/netcat0
        for commander in self.commanders:
            folder_name = commander.env.env['home_dir'].split('/')[-1]
            commander.env.env['home_dir'] = os.path.join(self.env.env['home_dir'],
                                                         folder_name)

    def configure(self):
        self._create_home_dir()
        self._create_conf_file()
        for commander in self.commanders:
            commander.configure()

    def run(self):
        cmd = self.commanders[0].run(execute=False)
        self.exe.execute(cmd)

    def _create_home_dir(self):
        if not os.path.exists(self.env.env['home_dir']):
            os.makedirs(self.env.env['home_dir'])

    def _create_conf_file(self):
        loader  = FileLoader(os.path.abspath(os.path.join(
            self.env.env['home_dir'], '../templates')))
        template = loader.load_template(self.env.env['conf_templ'])
        conf = template.render(self.env.env)
        with open(os.path.join(self.env.env['home_dir'],
                  self.env.env['conf_file']), 'w') as fd:
            fd.write(conf)


    def _destroy(self):
        shutil.rmtree(self.env.env['home_dir'])

