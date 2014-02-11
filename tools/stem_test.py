#!/usr/bin/env python3
from stem.control import Controller
import argparse


parser = argparse.ArgumentParser(description='stem controller script')
parser.add_argument('-o', type=str, help='o=[close, create...]')
args = parser.parse_args()

with Controller.from_port(port=9051) as controller:
    controller.authenticate()
    controller.set_conf('__DisablePredictedCircuits', '1')
    controller.set_conf('MaxOnionsPending', '0')
    controller.set_conf('newcircuitperiod', '999999')
    controller.set_conf('maxcircuitdirtiness', '99999')

    network = { desc.nickname: desc.fingerprint for desc in controller.get_network_statuses()}
    #print(network)


    if args.o == 'close':
        print('close all circuits')
        for circuit in controller.get_circuits():
            controller.close_circuit(circuit.id)

    if args.o == 'create':
        print('create new circuit')
        c_id = controller.extend_circuit(0, [network['Mallory17'], network['or15'], network['Mallory18']])

        # Malicious Exit Node Test Network
        #c_id = controller.extend_circuit(0, [network['or4'], network['or5'], network['Mallory8']])

        print(c_id)
        
    
    #print(controller.get_info('circuit-status'))
    for circuit in controller.get_circuits():
        print(circuit.purpose, end=': ')
        for node in circuit.path[:-1]:
            # node = (fingerprint, nick_name)
            print(node, end=' -> ')
        print(circuit.path[-1][1])

