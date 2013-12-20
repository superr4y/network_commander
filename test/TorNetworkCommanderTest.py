import sys, os, shutil, time
sys.path.append(os.path.abspath('../lib'))


os.environ['NETWORK_BASE_DIR'] = '/tmp/commander_test/net/'
if not os.path.exists(os.environ['NETWORK_BASE_DIR']):
    os.makedirs(os.environ['NETWORK_BASE_DIR'])

import unittest
import subprocess as sp

from Wrapper.Tor import *
from Environment.TorEnvironment import *
from Commander.TorNetworkCommander import *
from Commander.TorDirectoryAuthorityCommander import *






class TorNetworkCommanderTest(unittest.TestCase):

    def __init__(self, arg):
        super(TorNetworkCommanderTest, self).__init__(arg)
        self.tor_da = TorDirectoryAuthorityCommander()
        self.tor_net = TorNetworkCommander(das=[self.tor_da])

        self.tor_da._create_home_dir()
        self.create_template()

    def setup_keys(self):
        self.tor_da._create_conf_file()
        p = self.tor_da.exe.gen_authority_key(stdin=sp.PIPE)
        p.communicate(b'password\n')
        self.tor_da.exe.gen_fingerprint(stdin=sp.PIPE).communicate(b'\n')
        self.tor_da.update_new_tor_da(self.tor_da.env)

    
    def setUp(self):
        pass
        

    def tearDown(self):
        pass

    def test_tor_da_create_conf_file(self):
        self.tor_da._create_conf_file()
        with open(self.tor_da.env.abs_conf_file(), 'r') as fd:
            conf = fd.read()
        match = re.search(r'Nickname\s+(\S+)', conf)
        self.assertEqual(match.group(1), 'da') # update set_index(..)

    def test_tor_da_run(self):
        self.setup_keys()
        time.sleep(1)
        self.tor_da.run(stdin=sp.PIPE).communicate(b'\n')
        time.sleep(2)
        pid_file = os.path.join(self.tor_da.env['home_dir'], 'pid')

        self.assertTrue(os.path.exists(pid_file))
        
        with open(pid_file, 'r') as fd:
            pid = fd.read().rstrip()
        os.system('/usr/bin/kill {0}'.format(pid))
        
        
       

    def create_template(self):
        da_tmpl = '''
TestingTorNetwork 1
DataDirectory @home_dir
RunAsDaemon 1
ConnLimit 60
Nickname @nick_name
ShutdownWaitLength 0
PidFile @home_dir/pid
Log notice file @home_dir/notice.log
Log info file @home_dir/info.log
ProtocolWarnings 1
SafeLogging 0

SocksPort @socks_port
OrPort @or_port
Address @ip
ControlPort @control_port
DirPort @dir_port
#NOTE: Setting TestingServerConsensusDownloadSchedule doesn't
#      help -- dl_stats.schedule is not DL_SCHED_CONSENSUS
#      at boostrap time.
TestingServerDownloadSchedule 10, 2, 2, 4, 4, 8, 13, 18, 25, 40, 60

AuthoritativeDirectory 1
V3AuthoritativeDirectory 1
ContactInfo auth@test.test
ExitPolicy reject *:*
TestingV3AuthInitialVotingInterval 300
TestingV3AuthInitialVoteDelay 2
TestingV3AuthInitialDistDelay 2
TestingV3AuthVotingStartOffset 0
'''
        with open(self.tor_da.env.abs_conf_tmpl(), 'w') as fd:
            fd.write(da_tmpl)
        

if __name__ == '__main__':
    unittest.main()
