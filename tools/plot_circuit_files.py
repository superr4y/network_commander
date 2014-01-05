#!/usr/bin/env python3

from pylab import *
import sys



def parse_time_from_file(file):
    time = []
    for line in  open(file, 'r'):
        l = line.split(',')
        if(len(l)>2):
            time.append(float(l[1]))
    return time


def main():
        


    files = ['circuit_2147483920.log', 'circuit_2147497548.log', 'circuit_2147503819.log',
             'circuit_2147483921.log', 'circuit_2147497549.log', 'circuit_2147503820.log']
    #files = sys.argv[1:]
    count = 1
    
    for file in files:
        print('parse file {0}'.format(file))
        X = parse_time_from_file('/tmp/circuits/{0}'.format(file))
        Y = [count]*len(X)
        scatter(X, Y)
        count += 1
    
    savefig('/tmp/diff.png')
    
if __name__ == '__main__':
    main()