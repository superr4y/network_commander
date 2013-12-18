#!/usr/bin/env python3
import os

class LxcEnvironment:
    def __init__(self):
        self.env = {'home_dir': os.path.join(os.path.abspath(
            os.environ['NETWORK_BASE_DIR']), 'lxc'),
                    'ip': '10.0.0.2',
                    'gw_ip': '10.0.0.1',
                    'conf_file': 'lxc.conf',
                    'conf_templ': 'lxc.conf.tmpl',
                    'name': 'vm0'
        }

    def conf_file(self):
        return os.path.join(self.env['home_dir'], self.env['conf_file'])
        
