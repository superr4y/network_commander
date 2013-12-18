import sys, os
sys.path.append(os.path.abspath('lib'))
os.environ['NETWORK_BASE_DIR'] = os.path.join(os.getcwd(), 'net')
if not os.path.exists(os.environ['NETWORK_BASE_DIR']):
    os.mkdir(os.environ['NETWORK_BASE_DIR'])

import argparse


##### config #####
from Commander.LxcCommander  import LxcCommander
from Commander.NetCatCommander  import NetCatCommander

lxc1 = LxcCommander([NetCatCommander()])
lxc2 = LxcCommander([NetCatCommander()])

commanders = [lxc1, lxc2]

##### config #####


class Mode:
    def configure(self):
        print('config...')
        index = 0
        for commander in commanders:
            commander.env.set_index(index)
            commander.configure()
            index+=1

    def run(self):
        print('run...')
        index = 0
        for commander in commanders:
            commander.env.set_index(index)
            commander.run()
            index += 1

    def stop(self):
        print('stop...')
        index = 0
        for commander in commanders:
            commander.env.set_index(index)
            commander.exe.stop() # kill lxc container and everything in it

    def info(self):
        print('info...')
        #TODO: at the moment, info works only if the commander is a LxcCommander
        index = 0
        for commander in commanders:
            commander.env.set_index(index)
            msg = '[+] {0} => {1}'.format(commander.env['name'], 
                            'running' if commander.exe._is_running() else 'stopped')
            print(msg)
            index += 1

    def manage(self):
        print('manage...')


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
