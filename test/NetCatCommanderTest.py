import sys, os
sys.path.append(os.path.abspath('../lib'))

import re
from subprocess import Popen
import subprocess as sp
import unittest
from Commander.NetCatCommander import *


class NetCatCommanderTest(unittest.TestCase):

    def __init__(self, arg):
        super(NetCatCommanderTest, self).__init__(arg)
        os.environ['NETWORK_BASE_DIR'] = '/tmp/net/'
        self.base_dir = os.path.join(os.environ['NETWORK_BASE_DIR'], 'netcat')
        
        self.create_template()
       

    def create_template(self):
        template_str = 'port = @port\nhome_dir = @home_dir\n'
        template_dir = os.path.join(os.environ['NETWORK_BASE_DIR'],'templates')
        if not os.path.exists(template_dir):
            os.makedirs(template_dir)
        with open(os.path.join(template_dir, 'nc.conf.tmpl'), 'w') as fd:
            fd.write(template_str)
        
        
    def setUp(self):
        self.nc_commander = NetCatCommander()
        self.nc_commander._create_home_dir()

    def tearDown(self):
        pass
        #Popen('killall nc', shell=True)
        #self.nc_commander._destroy()

    def test_network_base_dir(self):
        self.assertEqual(self.nc_commander.env.env['home_dir'],
                          self.base_dir)
        self.assertTrue(os.path.exists(self.base_dir))

    def test_create_conf_file(self):
        self.nc_commander._create_conf_file()
        conf_file = os.path.join(self.base_dir, 'nc.conf')
        self.assertTrue(os.path.exists(conf_file))
        
        with open(conf_file, 'r') as fd:
            conf_str = fd.read()
        match = re.search(r'port = (\S+)', conf_str)
        self.assertEqual(match.group(1), '6666')
        match = re.search(r'home_dir = (\S+)', conf_str)
        self.assertEqual(match.group(1), self.nc_commander.env.env['home_dir'])

    def test_run(self):
        self.nc_commander.run()
        output = Popen('ps aux', shell=True, stdout=sp.PIPE).communicate()[0]
        match = re.search(r'nc -lnvp 666', output.decode('utf-8'))
        self.assertTrue(match)
        Popen('killall nc', shell=True, stdout=sp.PIPE, stderr=sp.STDOUT)
        


if __name__ == '__main__':
    unittest.main()
