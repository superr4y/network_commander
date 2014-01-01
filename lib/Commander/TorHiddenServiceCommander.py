#!/usr/bin/env python3

#sys.path.append(os.path.abspath('../'))
from Environment.TorEnvironment import TorEnvironment
from Commander.TorBaseCommander import TorBaseCommander
from Wrapper.Tor import Tor


class TorHiddenServiceCommander(TorBaseCommander):
    def __init__(self, **kwargs):
        '''
        doc doc doc
        '''
        if 'nick_name' not in kwargs:
            kwargs['nick_name'] = 'hs'

        super(TorHiddenServiceCommander, self).__init__(
                        conf_tmpl='torrc.hs.tmpl', **kwargs)

    def run(self, **kwargs):
        return self.exe.run_tor_hs(**kwargs)
