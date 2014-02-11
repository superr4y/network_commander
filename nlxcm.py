#!/usr/bin/env python3

import sys, os
sys.path.append(os.path.abspath('lib'))
os.environ['NETWORK_BASE_DIR'] = os.path.join(os.getcwd(), 'net')
if not os.path.exists(os.environ['NETWORK_BASE_DIR']):
    os.makedirs(os.environ['NETWORK_BASE_DIR'])

import argparse, traceback
from functools import wraps
from collections import OrderedDict

from tkinter import *
import tkinter.ttk as ttk
from Gui.CommanderFrame  import CommanderFrame


##### config #####
from Commander.LxcCommander  import LxcCommander
from Commander.NetCatCommander  import NetCatCommander
from Commander.TorNetworkCommander import TorNetworkCommander
from Commander.TorDirectoryAuthorityCommander import TorDirectoryAuthorityCommander
from Commander.TorOnionRouterCommander import TorOnionRouterCommander
from Commander.TorOnionProxyCommander import TorOnionProxyCommander
from Commander.TorHiddenServiceCommander import TorHiddenServiceCommander
from Commander.DnsCommander import DnsCommander
from Commander.HttpCommander import HttpCommander


commanders = []


#TODO: this decorator sucks, get rid of it
def all_commanders(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(func.__name__)
        index = 0
        for commander in commanders:
            i = None
            kwargs['commander'] = commander
            if hasattr(commander, 'env'):
                # All other Commanders
                index = commander.env.set_index(index)
            else:
                # TorNetworkCommander
                index = commander.set_index(index)

            ret = func(*args, **kwargs)

            if ret:
                #pprint.pprint(ret)
                kwargs['ret'] = ret
        return ret
    return wrapper


class Mode:
    
    def __init__(self, conf_file):
        self.conf_file = conf_file

    @all_commanders
    def configure(self, commander=None):
        os.setuid(1000)
        commander.configure()
        # at that point commander have the right IP and Name
        # commanders[0] = dns
        commanders[0].commanders[0].addDnsEntry(commander.getDns())

    @all_commanders
    def start(self, commander=None):
        commander.run()

    @all_commanders
    def stop(self, commander=None):
        if hasattr(commander, 'exe'):
            # kill lxc container and everything in it
            commander.exe.stop()
        elif hasattr(commander, 'stop'):
            commander.stop()

    @all_commanders
    def info(self, commander=None):
        msg = ''
        if hasattr(commander, 'env'):
            msg = '[+] {0} => {1}\n'.format(commander.env['nick_name'], 
                            'running' if commander.exe._is_running() else 'stopped')
        elif hasattr(commander, 'info'):
            for state in commander.info():
                msg += '[+] {0} => {1}\n'.format(state[0], 
                             'running' if state[1] else 'stopped')
        print(msg, end='')

    @all_commanders
    def clear(self, commander=None):
        commander._destroy()

    @all_commanders
    def _get_tree(self, commander=None, ret=None):
        if not ret:
            ret = OrderedDict()
        ret.update(commander.tree())
        return ret

    def gui(self):
        tree = self._get_tree()
        #pprint.pprint(tree)
        root = Tk()
        frame = CommanderFrame(root, tree, self.conf_file)
        frame.grid(row=0, column=0)
        root.mainloop()

    @all_commanders
    def gen_data(self, commander=None):
        if isinstance(commander, TorNetworkCommander):
            commander.gen_data()


       
       

def main():
    
    parser = argparse.ArgumentParser(description='One Commander to rule them all')
    parser.add_argument('mode', type=str,
                    help='possible modes are [{0}]'.format(', '.join(
                            (f for f in Mode.__dict__ if f[0] != '_')
                    )))
    parser.add_argument('-f', type=str, help='config file default = conf/config.py',
                    default='conf/config.py')

    args = parser.parse_args()
    mode = Mode(args.f)

    with open(args.f, 'r') as fd:
        # redefine commanders list
        exec(fd.read())
    
    try:
        getattr(mode, args.mode)()
    except AttributeError as e:
        parser.print_help()
        traceback.print_exc(file=sys.stdout)
        



if __name__ == '__main__':
    main()
