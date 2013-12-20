#!/usr/bin/env python3
from quik import FileLoader
import subprocess as sp
import quik
import os, sys, shutil
from itertools import chain
#sys.path.append(os.path.abspath('../'))
from Environment.LxcEnvironment import LxcEnvironment
from Wrapper.Lxc import Lxc


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
        self.das = das
        self.ors = ors
        self.ops = ops
        self.bs = bs
        self.hs = hs
        self.all_nodes = chain(self.das, self.ors, self.ops, self.bs, self.hs)


    def configure(self):
        for node in self.all_nodes:
            # set_index()???
            node.configure()

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
            ret.append((node.env['name'], node.env._is_running()))
        return ret


