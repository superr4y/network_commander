import sys, os
sys.path.append(os.path.abspath('../lib'))

import unittest
from Environment.LxcEnvironment import LxcEnvironment


class LxcEnvironmentTest(unittest.TestCase):

    def __init__(self, arg):
        super(LxcEnvironmentTest, self).__init__(arg)
        os.environ['NETWORK_BASE_DIR'] = '/tmp/net/'
        self.home_dir = os.path.join(os.environ['NETWORK_BASE_DIR'], 'lxc666')
        
        
    def setUp(self):
        self.env = LxcEnvironment()
        self.env.set_index(666)

    def tearDown(self):
        pass

    def test_home_dir(self):
        self.assertEqual(self.env['home_dir'], self.home_dir)

    def test_abs_conf_file(self):
        self.assertEqual(self.env.abs_conf_file(),
                         os.path.join(self.home_dir, 'lxc.conf'))

    def test_abs_conf_tmpl(self):
        self.assertEqual(self.env.abs_conf_tmpl(),
                         os.path.join(os.environ['NETWORK_BASE_DIR'],
                                      'templates' , 'lxc.conf.tmpl'))

    def test_ip_and_name(self):
        self.assertEqual(self.env['ip'], '10.0.0.668')
        self.assertEqual(self.env['name'], 'lxc666')
 
        


if __name__ == '__main__':
    unittest.main()
