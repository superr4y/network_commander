import sys, os
sys.path.append(os.path.abspath('../lib'))

import unittest, time
from Wrapper.Lxc import *


class WrapperLxcTest(unittest.TestCase):

    def __init__(self, arg):
        super(WrapperLxcTest, self).__init__(arg)
        self.conf_ok = 'lxc.conf'
        self.conf_bad = 'lxcb.conf'
        self.lxc = Lxc(self.conf_ok)
    
    def setUp(self):
        pass
        

    def tearDown(self):
        self.lxc.stop()

    def test_execute(self):
        self.lxc.execute('sleep 1000')
        self.assertTrue(self.lxc._is_running())
        self.assertRaises(LxcIsAlreadRunningException, self.lxc.execute,
                          ('sleep 1000'))
        
    #def test_attach(self):
    #    self.lxc.execute(['sleep', '1000'])
    #    self.lxc.attach()
    #    self.lxc.stop()

    def test_stop(self):
        self.lxc.execute('sleep 1000')
        self.lxc.stop()
        time.sleep(3) # because everything runs in background
        self.assertFalse(self.lxc._is_running())

    def test_is_running(self):
        self.assertFalse(self.lxc._is_running())
        self.lxc.execute('sleep 1000')
        self.assertTrue(self.lxc._is_running())
        
    def test_lxc_name(self):
        lxc = Lxc(self.conf_ok)
        self.assertEqual(lxc._lxc_name(), 'vm0')

        lxc = Lxc(self.conf_bad)
        self.assertRaises(LxcConfException, lxc._lxc_name)



if __name__ == '__main__':
    unittest.main()

    
