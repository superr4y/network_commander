import sys, os
sys.path.append(os.path.abspath('../lib'))

import re
from subprocess import Popen
import subprocess as sp
import unittest
from Commander.NetCatCommander import *
from Commander.LxcCommander import *


class LxcCommanderTest(unittest.TestCase):

    def __init__(self, arg):
        super(LxcCommanderTest, self).__init__(arg)
        os.environ['NETWORK_BASE_DIR'] = '/tmp/net/'
        self.base_dir = os.path.join(os.environ['NETWORK_BASE_DIR'], 'lxc')
        
        self.create_template()
       

    def create_template(self):
        template_str = '''
lxc.utsname = @name
lxc.rootfs = / 
lxc.pts=1024
lxc.tty=1
lxc.console=/var/log/lxc/test0.console 

lxc.network.type = veth 
lxc.network.veth.pair = veth0
lxc.network.flags = up  
lxc.network.link = br0 
lxc.network.name = eth0 
lxc.network.ipv4 = @ip
lxc.network.ipv4.gateway = @gw_ip
'''
        template_dir = os.path.join(os.environ['NETWORK_BASE_DIR'],'templates')
        if not os.path.exists(template_dir):
            os.makedirs(template_dir)
        with open(os.path.join(template_dir, 'lxc.conf.tmpl'), 'w') as fd:
            fd.write(template_str)

        # NetCat template
        template_str = 'port = @port\nhome_dir = @home_dir\n'
        if not os.path.exists(template_dir):
            os.makedirs(template_dir)
        with open(os.path.join(template_dir, 'nc.conf.tmpl'), 'w') as fd:
            fd.write(template_str)
        
        
        
    def setUp(self):
        self.lxc_commander = LxcCommander([NetCatCommander()])
        self.lxc_commander._create_home_dir()

    def tearDown(self):
        pass
        #Popen('killall nc', shell=True)
        #self.nc_commander._destroy()

    def test_network_base_dir(self):
        self.assertEqual(self.lxc_commander.env.env['home_dir'],
                         self.base_dir)
        self.assertTrue(os.path.exists(self.base_dir))
        

    def test_create_conf_file(self):
        self.lxc_commander._create_conf_file()
        conf_file = os.path.join(self.base_dir, 'lxc.conf')
        self.assertTrue(os.path.exists(conf_file))
        
        with open(conf_file, 'r') as fd:
            conf_str = fd.read()
        match = re.search(r'lxc.utsname = (\S+)', conf_str)
        self.assertEqual(match.group(1), self.lxc_commander.env.env['name'])
        match = re.search(r'lxc.network.ipv4 = (\S+)', conf_str)
        self.assertEqual(match.group(1), self.lxc_commander.env.env['ip'])

    def test_run(self):
        self.lxc_commander.run()
        self.assertTrue(self.lxc_commander.exe._is_running())
        self.lxc_commander.exe.stop()

    def test_configure(self):
        self.lxc_commander.configure()
        self.assertEqual(self.lxc_commander.commanders[0].env.env['home_dir'],
                          os.path.join(self.base_dir, 'netcat'))
        self.assertTrue(os.path.exists(os.path.join(self.base_dir, 'netcat')))

if __name__ == '__main__':
    unittest.main()
