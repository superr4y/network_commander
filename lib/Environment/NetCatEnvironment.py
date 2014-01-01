#!/usr/bin/env python3
import os
from .EnvironmentBase import EnvironmentBase

class NetCatEnvironment(EnvironmentBase):
    def __init__(self, **kwargs):
        super(NetCatEnvironment, self).__init__(
            home_dir='netcat', conf_file='nc.conf')
        self.update({'port': '6666', 'nick_name': 'netcat'})
        self.update(**kwargs)

            

    
    def set_index(self, index, parent_env):
        self['index'] = index
        folder_name = self['home_dir'].split('/')[-1]
        self['home_dir'] = '{0}_{1}'.format(
            os.path.join(parent_env['home_dir'], folder_name), index)

        return index

    def __str__(self):
        return 'netcat{0}'.format(self['index'])
