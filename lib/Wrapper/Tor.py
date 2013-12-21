#!/usr/bin/env python3
import subprocess as sp
import sys, os
#sys.path.append(os.path.abspath('../'))
from .Wrapper import ExecuteOrNot, Debug


class Tor:
    def __init__(self, env):
        """abcd
        """
        self.env = env
        self.tor_start = 'su user -c "{0} -f {1}"'

    
    @ExecuteOrNot   
    def gen_authority_key(self, **kwargs):
        if not os.path.exists(self.env.abs_keys_folder()):
            os.makedirs(self.env.abs_keys_folder())
        cmd = '{0} --create-identity-key --passphrase-fd 0 -i {1} -s {2} -c {3} -a {4}:{5}'
        cmd = cmd.format(
            self.env['tor_gencert_bin'], self.env.abs_id_file(),
            self.env.abs_sk_file(), self.env.abs_cert_file(),
            self.env['ip'], self.env['dir_port'])
        return cmd

    @ExecuteOrNot
    def gen_fingerprint(self, **kwargs):
        cmd = '{0} --quiet -f {1} --list-fingerprint --orport 1 --dirserver "{2} {3}:{4} {5}"'.format(
            self.env['tor_bin'], self.env.abs_conf_file(),
            self.env['nick_name'], self.env['ip'],
            self.env['dir_port'], self.env.fingerprint_from_cert_file())
        return cmd

    @ExecuteOrNot
    def run_tor_da(self, **kwargs):
        return self.tor_start.format(self.env['tor_bin'],
                                     self.env.abs_conf_file())

    @ExecuteOrNot
    def run_tor_or(self, **kwargs):
        return self.tor_start.format(self.env['tor_bin'],
                                     self.env.abs_conf_file())


    @ExecuteOrNot
    def run_tor_op(self, **kwargs):
        return self.tor_start.format(self.env['tor_bin'],
                                     self.env.abs_conf_file())



if __name__ == '__main__':
    pass

