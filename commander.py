import sys, os
sys.path.append(os.path.abspath('lib'))
os.environ['NETWORK_BASE_DIR'] = os.path.join(os.getcwd(), 'net')
if not os.path.exists(os.environ['NETWORK_BASE_DIR']):
    os.makedirs(os.environ['NETWORK_BASE_DIR'])

import argparse
from functools import wraps


##### config #####
from Commander.LxcCommander  import LxcCommander
from Commander.NetCatCommander  import NetCatCommander

lxc1 = LxcCommander(NetCatCommander())
lxc2 = LxcCommander(NetCatCommander())

commanders = [lxc1, lxc2]

##### config #####



def all_commanders(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(func.__name__)
        index = 0
        for commander in commanders:
            kwargs['commander'] = commander
            commander.env.set_index(index)
            func(*args, **kwargs)
            index += 1
    return wrapper


class Mode:
    @all_commanders
    def configure(self, commander=None):
        commander.configure()

    @all_commanders
    def run(self):
        commander.run()

    @all_commanders
    def stop(self, commander=None):
        # kill lxc container and everything in it
        commander.exe.stop()

    @all_commanders
    def info(self, commander=None):
        #TODO: at the moment, info works only if the commander is a LxcCommander
        msg = '[+] {0} => {1}'.format(commander.env['name'], 
                            'running' if commander.exe._is_running() else 'stopped')
        print(msg)

    @all_commanders
    def manage(self, commander=None):
        print(commander)


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
        print(e)



if __name__ == '__main__':
    main()
