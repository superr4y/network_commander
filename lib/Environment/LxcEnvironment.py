#!/usr/bin/env python3
import os
from .EnvironmentBase  import EnvironmentBase

class LxcEnvironment(EnvironmentBase):
    def __init__(self, envs=[], *args):
        super(LxcEnvironment, self).__init__(
            home_dir='lxc',
            conf_file='lxc.conf')
        
        self.envs = envs

        self.update({
                    'ip': '10.0.0.2',
                    'gw_ip': '10.0.0.1',
                    'name': 'lxc'})

        self.update(*args)

    def set_index(self, index):
        super(LxcEnvironment, self).set_index(index)
        ip = '.'.join(self['ip'].split('.')[:3])
        self['ip'] = '{0}.{1}'.format(ip, index+2)
        self['name'] = '{0}{1}'.format(self['name'], index)

        lxc_index = 0
        for env in self.envs:
            folder_name = env['home_dir'].split('/')[-1]
            env['home_dir'] = os.path.join(self['home_dir'], folder_name)
            env.set_index('{0}_{1}'.format(index, lxc_index))
