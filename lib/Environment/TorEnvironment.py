#!/usr/bin/env python3
import os, re
from functools import wraps
from .EnvironmentBase import EnvironmentBase
from Wrapper.Wrapper import abs_path


class TorEnvironment(EnvironmentBase):
    def __init__(self, **kwargs):
        super(TorEnvironment, self).__init__(
            home_dir='tor', conf_file='torrc')
        keys_folder = 'keys'
        self.update({'tor_bin': 'tor',
                     'tor_gencert_bin': 'tor-gencert',
                     'keys_folder': keys_folder,
                     'id_file': 'authority_identity_key',
                     'sk_file': 'authority_signing_key',
                     'cert_file': 'authority_certificate',
                     'ip': '10.0.0.2',
                     'dir_port': 9000,
                     'or_port': 8000,
                     'socks_port': 9050,
                     'control_port': 9051,
                     'nick_name': 'xxx' # update if set_index(..)
                 })
        self.update(**kwargs)


    @abs_path
    def abs_id_file(self):
        return os.path.join(self['keys_folder'], self['id_file'])

    @abs_path
    def abs_sk_file(self):
        return os.path.join(self['keys_folder'], self['sk_file'])

    @abs_path
    def abs_cert_file(self):
        return os.path.join(self['keys_folder'], self['cert_file'])

    @abs_path
    def abs_keys_folder(self):
        return self['keys_folder']

    def fingerprint_from_cert_file(self):
        #fingerprint 899F56BD2F47188F9297830D856303CA79D419D8
        with open(self.abs_cert_file(), 'r') as fd:
            cert = fd.read()
        match = re.search(r'fingerprint\s+(\S+)', cert)
        return match.group(1)

    def fingerprint_from_file(self):
        #./fingerprint
        with open(os.path.join(self['home_dir'], 'fingerprint'), 'r') as fd:
            fp = fd.read()
        match = re.search(r'\S+\s+(\S+)', fp)
        return match.group(1)
            
    def torrc_da_entry(self):
        '''
        This method should only be called from a DirectoryAuthority environment
        '''
        ret = 'DirAuthority {0} orport={1} no-v2 hs v3ident={2} {3}:{4} {5}'.format(
            self['nick_name'], self['or_port'], 
            self.fingerprint_from_cert_file(),
            self['ip'], self['dir_port'], self.fingerprint_from_file())
        return ret
