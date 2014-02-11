#!/usr/bin/env python3

#from pylab import *
import matplotlib.pyplot as plt
import sys, re




def parse_time_from_file(file):
    time = []
    for line in  open(file, 'r'):
        l = line.split(',')
        if(len(l)>2):
            time.append(float(l[1]))
    return time


def partitionate_heigh_score_circuits(score_list):
    heigh_score_list = []
    for pair in score_list:
        c1, c2 , score = pair.split(' ')
        if(int(score) > 1000):
            heigh_score_list.append((c1, c2, score))           
    circuit_linked = set()
    for pair in heigh_score_list:
        match_set= set()
        for pp in heigh_score_list:
            if pair == pp:
                continue
            if pair[0] in pp or pair[1] in pp:
                match_set.add(pp[0])
                match_set.add(pp[1])
        match_set.add(pair[0])
        match_set.add(pair[1])
        circuit_linked.add(frozenset(match_set))
    return circuit_linked

def main():

    files = sys.argv[1:]
    count = 1
    labels = ['']
    score_list = []
    """    with open('score.txt', 'r') as fd:
            for line in fd:
                score_list.append(line)
        for x in partitionate_heigh_score_circuits(score_list):
            print(x)
    """    
    for file in files:
        print('parse file {0}'.format(file))
        X = parse_time_from_file('../circuits/{0}'.format(file))
        Y = [count]*len(X)
        plt.plot(X, Y, 'bo')
        count += 1
        match = re.match(r'm(\d+)_circuit_(\d+).log', file)
        #match = re.match(r'circuit_(\d+).log', file)
        labels.append('Mallory'+match.group(1)+'->'+match.group(2))
        #labels.append('Mallory -> '+match.group(1))
    

    plt.ylim([0, count])
    plt.yticks(range(count), labels, fontsize=15)
    plt.grid(True)
    plt.xlabel('Time in ms', fontsize=20)
    plt.ylabel('Circuit IDs', fontsize=20)

    #ax = plt.subplot(1, 1, 1)
    #p1, p2 = ax.plot([1, 2, 3], 'ro'), ax.plot([1, 2, 3], 'bo')
    #ax.legend([p1, p2], ['Mallory9', 'Mallory10'])

    plt.show()    
    
if __name__ == '__main__':
    main()
