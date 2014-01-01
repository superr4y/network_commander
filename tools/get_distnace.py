#!/usr/bin/env python3

from pylab import *
from scipy import spatial
import numpy as np

import argparse


class Distance:
    def __init__(self, mul=10000, distance_upper_bound=10000):
        self.mul = mul
        self.distance_upper_bound = distance_upper_bound
        
        # cells for circuit 1 and 2
        self.cells_c1 = []
        self.cells_c2 = []


    def _parse_logfile(self, file_name, cells_list):
        with open(file_name, 'r') as fd:
            for cell in fd:
                cells_list.append(cell.rstrip().split(','))

    def parse_logfile(self, c1, c2):
        '''
        Read c1 and c2 file and append parsed result to cells_cx.
        Build x1/y1 and x2/y2 out of cells_c1/2
        '''
        self._parse_logfile(c1, self.cells_c1)
        self._parse_logfile(c2, self.cells_c2)
        
        # cell[1] = time im ms
        self.x1 = [float(cell[1])*self.mul for cell in self.cells_c1 if len(cell) > 3]
        self.y1 = [1]*len(self.x1)

        self.x2 = [float(cell[1])*self.mul for cell in self.cells_c2 if len(cell) > 3]
        self.y2 = [1]*len(self.x2)

        # make sure that x2/y2 is the shorter list
        tmp_x = self.x1
        tmp_y = self.y1
        if len(self.x1) < len(self.x2):
            self.x1 = self.x2
            self.y1 = self.y2
            self.x2 = tmp_x
            self.y2 = tmp_y
            

    def calc_score(self):
        score = 0

        for x, y in zip(self.x2, self.y2):
            if len(self.x1) == 0 or len(self.y1) == 0:
                break
            ckdtree = spatial.cKDTree(np.array([ [a, b] for a, b in zip(self.x1, self.y1) ])) # this is expensive
            best = ckdtree.query(np.array([x, y]), k=1, distance_upper_bound=self.distance_upper_bound)
            #print(point)
            if best[0] != inf:
                self.x1.pop(best[1])
                self.y1.pop(best[1])
                score += 1

        return score
    


def main():
    parser = argparse.ArgumentParser(description='One Commander to rule them all')
    parser.add_argument('circuit_log_1', type=str,
                        help='file name from circuit logfile 1')
    parser.add_argument('circuit_log_2', type=str,
                        help='file name from circuit logfile 2')

    args = parser.parse_args()    

    dist = Distance()
    # circuit_2147511197.log
    #dist.parse_logfile('circuit_2147495958.log', 'circuit_27406.log')
    dist.parse_logfile(args.circuit_log_1, args.circuit_log_2)
    print(dist.calc_score())

if __name__ == '__main__':
    main()
