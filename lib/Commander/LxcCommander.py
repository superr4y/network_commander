#!/usr/bin/env python3
from quik import FileLoader
from collections import OrderedDict
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
        if len(self.commanders) > 1:
            for commander in self.commanders[1:]:
                cmd = '{0}'.format(commander.run(execute=False))
                self.exe.attach(cmd=cmd)
                
        
    def stop(self):
        self.exe.stop()

    def tree(self):
        ret = OrderedDict()
        dns = self.getDns()
        ret[dns] = {'container': self}
        for commander, env in zip(self.commanders, self.env.envs):
            ret[dns].update({str(env): commander})
        return ret

    def attach(self, **kwargs):
        if not self.exe._is_running():
            print('{0} is not running execute bash'.format(self.getDns()))
            self.exe.execute('bash')
        return self.exe.attach(**kwargs)
        

    def _create_home_dir(self):
        if not os.path.exists(self.env['home_dir']):
            os.makedirs(self.env['home_dir'])
            os.symlink(os.path.join(self.env['home_dir'], '../../tools'),
                    os.path.join(self.env['home_dir'],'tools'))


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
