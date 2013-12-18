import sys, os
sys.path.append(os.path.abspath('../lib'))

import unittest
from Environment.NetCatEnvironment import NetCatEnvironment


class NetCatEnvironmentTest(unittest.TestCase):

    def __init__(self, arg):
        super(NetCatEnvironmentTest, self).__init__(arg)
        os.environ['NETWORK_BASE_DIR'] = '/tmp/net/'
        self.home_dir = os.path.join(os.environ['NETWORK_BASE_DIR'], 'netcat666')
        
        
    def setUp(self):
        self.env = NetCatEnvironment()
        self.env.set_index(666)

    def tearDown(self):
        pass

    def test_home_dir(self):
        self.assertEqual(self.env['home_dir'], self.home_dir)

    def test_abs_conf_file(self):
        self.assertEqual(self.env.abs_conf_file(),
                         os.path.join(self.home_dir, 'nc.conf'))

    def test_abs_conf_tmpl(self):
        self.assertEqual(self.env.abs_conf_tmpl(),
                         os.path.join(os.environ['NETWORK_BASE_DIR'],
                                      'templates' , 'nc.conf.tmpl'))
 
        


if __name__ == '__main__':
    unittest.main()
