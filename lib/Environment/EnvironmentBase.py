#!/usr/bin/env python3
import os
from Wrapper.Wrapper import need_index


#TODO: Test if self.index is set and raise exception otherwise (__getattr__)
class EnvironmentBase(dict):
    def __init__(self, *args, home_dir='', conf_file=''):
        '''
        home_dir: e.g. netcat, lxc ..
        conf_file: e.g. lxc.conf
        '''
        self.update({'home_dir': os.path.join(os.path.abspath(
            os.environ['NETWORK_BASE_DIR']), home_dir),
                    'conf_file': conf_file,
                    'conf_tmpl': '{0}.tmpl'.format(conf_file)
        })

    @need_index
    def abs_conf_file(self):
        return os.path.join(self['home_dir'], self['conf_file'])

    @need_index
    def abs_conf_tmpl(self):
        return os.path.abspath(os.path.join(os.environ['NETWORK_BASE_DIR'],
                            '../templates', self['conf_tmpl']))

    def set_index(self, index, parent_env):
        self['index'] = index
        folder_name = self['home_dir'].split('/')[-1]
        self['home_dir'] = '{0}_{1}'.format(
            os.path.join(parent_env['home_dir'], folder_name), index)
        self['ip'] = parent_env['ip']

        return index
