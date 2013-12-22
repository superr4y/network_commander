#!/usr/bin/env python3
import os
from .EnvironmentBase import EnvironmentBase
from Wrapper.Wrapper import abs_path, need_index


class DnsEnvironment(EnvironmentBase):
    def __init__(self, **kwargs):
        super(DnsEnvironment, self).__init__(
            home_dir='dns', conf_file='domain.conf')
        self.update({'dns_bin': os.path.join(os.getcwd(), 'minidns')})
        self.update(**kwargs)

    @need_index
    def __str__(self):
        return 'dns{0}'.format(self['index'])

    
