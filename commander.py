import sys, os
sys.path.append(os.path.abspath('lib'))
os.environ['NETWORK_BASE_DIR'] = os.path.join(os.getcwd(), 'net')
if not os.path.exists(os.environ['NETWORK_BASE_DIR']):
    os.makedirs(os.environ['NETWORK_BASE_DIR'])

import subprocess as sp
import argparse, traceback
from functools import wraps


##### config #####
from Commander.LxcCommander  import LxcCommander
from Commander.NetCatCommander  import NetCatCommander
from Commander.TorNetworkCommander import TorNetworkCommander
from Commander.TorDirectoryAuthorityCommander import TorDirectoryAuthorityCommander
from Commander.TorOnionRouterCommander import TorOnionRouterCommander
from Commander.TorOnionProxyCommander import TorOnionProxyCommander

nc = LxcCommander(NetCatCommander())
tor_net = TorNetworkCommander(
    das=[
        LxcCommander(TorDirectoryAuthorityCommander()),
        LxcCommander(TorDirectoryAuthorityCommander())
    ],
    ors=[
        LxcCommander(TorOnionRouterCommander()),
        LxcCommander(TorOnionRouterCommander())
    ],
    ops=[
        LxcCommander(TorOnionProxyCommander()),
        LxcCommander(TorOnionProxyCommander())
    ]
)

commanders = [tor_net, nc]

#tree = {
#    'lxc_0':{'obj': lxc_commander_obj, 'da_0': da_commander},
#    'lxc_1':{...}
#}

##### config #####



def all_commanders(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(func.__name__)
        index = 0
        for commander in commanders:
            i = None
            kwargs['commander'] = commander
            if hasattr(commander, 'env'):
                index = commander.env.set_index(index)
            else:
                index = commander.set_index(index)
            func(*args, **kwargs)
    return wrapper


class Mode:
    @all_commanders
    def configure(self, commander=None):
        commander.configure()

    @all_commanders
    def run(self, commander=None):
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
            msg = '[+] {0} => {1}\n'.format(commander.env['name'], 
                            'running' if commander.exe._is_running() else 'stopped')
        elif hasattr(commander, 'info'):
            for state in commander.info():
                msg += '[+] {0} => {1}\n'.format(state[0], 
                             'running' if state[1] else 'stopped')
        print(msg, end='')

    def manage(self, commander=None):
        user_input = None
        while user_input != 'exit':
            print('>>> ', end='')
            user_input = input().rstrip()
            if user_input == 'info':
                self.info()
            elif user_input.split(' ')[0] == 'a':
                print('attach {0}'.format(user_input.split(' ')))
                sp.Popen('gnome-terminal')
                
            




def main():
    mode = Mode()
    parser = argparse.ArgumentParser(description='One Commander to rule them all')
    parser.add_argument('mode', type=str,
                        help='posible modes are [{0}]'.format(', '.join(
                            (f for f in Mode.__dict__ if f[0] != '_')
                            )))

    args = parser.parse_args()
    
    try:
        getattr(mode, args.mode)()
    except AttributeError as e:
        parser.print_help()
        traceback.print_exc(file=sys.stdout)
        



if __name__ == '__main__':
    main()
