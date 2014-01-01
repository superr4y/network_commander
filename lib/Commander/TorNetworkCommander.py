#!/usr/bin/env python3
from itertools import chain
#sys.path.append(os.path.abspath('../'))
from Environment.TorEnvironment import TorEnvironment
from Wrapper.Tor import Tor


class TorNetworkCommander:
    def __init__(self, das=None, ors=None, ops=None, bs=None, hs=None):
        '''
        TorNetworkCommander is responseble for the entire Tor Network.
        This is a container commander which can capsulate lots
        of LXC Container. Because of this we need special functions
        e.g. info() => get state of all containers...
        TorNetworkCommander doesn't have a own environment, the only
        purporse is to manage and hide the complexity from the
        config file.


        das = [LxcCommander(TorDirecotryAuthorityCommander),..]
        ors = [LxcCommander(TorOnionRouterCommander),..]
        ops = [LxcCommander(TorOnionProxyCommander),..]
        bs =  [LxcCommander(TorBridgeCommander),..]
        hs  = [LxcCommander(TorHiddenServiceCommander),..]
        '''
        self.das = das if das else []
        self.ors = ors if ors else []
        self.ops = ops if ops else []
        self.bs = bs   if bs  else []
        self.hs = hs   if hs  else []
        self.all_nodes = [n for n in chain(self.das, self.ors, self.ops, self.bs, self.hs) if n]


    def configure(self):
        for da in self.das:
            da.configure()
        for node in self.all_nodes:
            if node not in self.das:
                node.configure()
            # append all DAs to all torrc
            for da in self.das:
                node.commanders[0].update_new_tor_da(da.commanders[0].env)

    def run(self):
        for node in self.all_nodes:
            node.run()
       
    def info(self):
        '''
        Returns the state of all containers as list of tubles
        [(name1, state1), (name2, state2), ...]
        '''
        ret = []
        for node in self.all_nodes:
            ret.append((node.env['nick_name'], node.exe._is_running()))
        return ret

    def _destroy(self):
        for node in self.all_nodes:
            node._destroy()

    def stop(self):
        for node in self.all_nodes:
            node.exe.stop() # kill lxc container and everything in it

    def set_index(self, index):
        for node in self.all_nodes:
            index = node.env.set_index(index)
        return index

    def tree(self):
        ret = {}
        for node in self.all_nodes:
            ret.update(node.tree())
        return ret

    def getDns(self):
        ret = ''
        for node in self.all_nodes:
            ret += node.getDns()+'\n'
        return ret

