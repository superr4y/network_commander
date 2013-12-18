#!/usr/bin/env python3
import os

class NetCatEnvironment:
    def __init__(self):
        self.env = {'home_dir': os.path.join(os.path.abspath(
            os.environ['NETWORK_BASE_DIR']), 'netcat'),
                    'port': '6666',
                    'conf_file': 'nc.conf',
                    'conf_templ': 'nc.conf.tmpl'
        }
        


    
