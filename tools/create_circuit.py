#!/usr/bin/env python3
from stem.control import Controller
import argparse
import sys



with Controller.from_port(port=9051) as controller:
    controller.authenticate()
    controller.set_conf('__DisablePredictedCircuits', '1')
    controller.set_conf('MaxOnionsPending', '0')
    controller.set_conf('newcircuitperiod', '999999')
    controller.set_conf('maxcircuitdirtiness', '99999')

    network = { desc.nickname: desc.fingerprint for desc in controller.get_network_statuses()}

    print('close all circuits')
    for circuit in controller.get_circuits():
        controller.close_circuit(circuit.id)

    if(len(sys.argv) == 4):
        print('create new circuit')
        c_id = controller.extend_circuit(0, [
            network[sys.argv[1].rstrip()], network[sys.argv[2].rstrip()], network[sys.argv[3].rstrip()]])
        print(c_id)
        
    
    #print(controller.get_info('circuit-status'))
    for circuit in controller.get_circuits():
        print(circuit.purpose, end=': ')
        for node in circuit.path[:-1]:
            # node = (fingerprint, nick_name)
            print(node, end=' -> ')
        print(circuit.path[-1][1])

