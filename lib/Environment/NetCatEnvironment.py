#!/usr/bin/env python3
import os
from .EnvironmentBase import EnvironmentBase

class NetCatEnvironment(EnvironmentBase):
    def __init__(self, *args):
        super(NetCatEnvironment, self).__init__(
            home_dir='netcat', conf_file='nc.conf')
        self.update({'port': '6666'})
        self.update(*args)

            

    
