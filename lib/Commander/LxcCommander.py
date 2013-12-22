#!/usr/bin/env python3
from quik import FileLoader
import subprocess as sp
import quik
import os, sys, shutil
sys.path.append(os.path.abspath('../'))
from Environment.LxcEnvironment import LxcEnvironment
from Wrapper.Lxc import Lxc


class LxcCommander:
    def __init__(self, *args, **kwargs):

        # get all environments from the other commanders
        envs = [com.env for com in args]

        self.env = LxcEnvironment(envs=envs)
        self.exe = Lxc(self.env)
        self.commanders = list(args)

        # e.g. /tmp/net/netcat0 => /home/net/lxc/netcat0
        for commander in self.commanders:
            folder_name = commander.env['home_dir'].split('/')[-1]
            commander.env['home_dir'] = os.path.join(self.env['home_dir'],
                                                         folder_name)

    def configure(self):
        self._create_home_dir()
        self._create_conf_file()
        for commander in self.commanders:
            commander.configure()

    def run(self):
        cmd = self.commanders[0].run(execute=False)
        self.exe.execute(cmd)

    def tree(self):
        ret = {}
        ret[self.getDns()] = {'container': self, str(self.env.envs[0]): self.commanders[0]}
        return ret

    def attach(self, **kwargs):
        return self.exe.attach(**kwargs)
        

    def _create_home_dir(self):
        if not os.path.exists(self.env['home_dir']):
            os.makedirs(self.env['home_dir'])

    def _create_conf_file(self):
        loader  = FileLoader('/')
        template = loader.load_template(self.env.abs_conf_tmpl())
        conf = template.render(self.env)
        with open(self.env.abs_conf_file(), 'w') as fd:
            fd.write(conf)


    def _destroy(self):
        shutil.rmtree(self.env['home_dir'])


    def __str__(self):
        return type(self).__name__

    def getDns(self):
        dns = '{0}.lo'.format(self.commanders[0].env.__str__())
        return '{0} {1}'.format(dns, self.env['ip'])
