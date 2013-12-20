import sys, os, shutil
sys.path.append(os.path.abspath('../lib'))


os.environ['NETWORK_BASE_DIR'] = '/tmp/commander_test/net/'
if not os.path.exists(os.environ['NETWORK_BASE_DIR']):
    os.makedirs(os.environ['NETWORK_BASE_DIR'])

import unittest
import subprocess as sp
from Wrapper.Tor import *
from Environment.TorEnvironment import *


class TorWrapperTest(unittest.TestCase):

    def __init__(self, arg):
        super(TorWrapperTest, self).__init__(arg)
        self.env = TorEnvironment()
        self.tor = Tor(self.env)

        self.base_dir = os.path.abspath(os.path.join(os.environ['NETWORK_BASE_DIR'], 'tor'))
    
    def setUp(self):
        pass
        

    def tearDown(self):
        key_folder = os.path.join(self.base_dir, 'keys')
        #shutil.rmtree(key_folder)

    def setup_keys(self):
        p = self.tor.gen_authority_key(stdin=sp.PIPE)
        p.communicate(b'password\n')

    def test_gen_authority_key(self):
        key_folder = os.path.join(self.base_dir, 'keys')
        cmd1 = self.tor.gen_authority_key(execute=False)
        cmd2 = 'tor-gencert --create-identity-key --passphrase-fd 0 -i {0}/{1} -s {2}/{3} -c {4}/{5} -a {6}'
        cmd2 = cmd2.format(key_folder, 'authority_identity_key',
                           key_folder, 'authority_signing_key',
                           key_folder, 'authority_certificate',
                           '10.0.0.2:9000')
        self.maxDiff = None
        self.assertEqual(cmd1, cmd2)

        p = self.tor.gen_authority_key(stdin=sp.PIPE)
        p.communicate(b'password\n')
        self.assertTrue(os.path.exists(self.tor.env.abs_id_file()))
        
        
    def test_get_fingerprint_from_cert_file(self):
        self.setup_keys()
        fp = self.tor.env.fingerprint_from_cert_file()
        self.assertEqual(len(fp), 40)

    def test_gen_fingerprint(self):
        self.setup_keys()
        p = self.tor.gen_fingerprint(stdin=sp.PIPE)
        p.communicate(b'\n')
        self.assertEqual(len(self.tor.env.fingerprint_from_file()), 40)

        
        



if __name__ == '__main__':
    unittest.main()

    
