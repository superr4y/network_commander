#!/usr/bin/env python3
import os
from .EnvironmentBase import EnvironmentBase
from Wrapper.Wrapper import need_index

class HttpEnvironment(EnvironmentBase):
    def __init__(self, **kwargs):
        super(HttpEnvironment, self).__init__(
            home_dir='http', conf_file='lighttpd.conf')
        self.update({'port': '80', 'nick_name': 'http'})
        self.update(**kwargs)

            

    
    def set_index(self, index, parent_env):
        self['index'] = index
        folder_name = self['home_dir'].split('/')[-1]
        self['home_dir'] = '{0}_{1}'.format(
            os.path.join(parent_env['home_dir'], folder_name), index)

        return index

    @need_index
    def __str__(self):
        return 'http{0}'.format(self['index'])
