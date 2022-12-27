from helper import *

# This module helps determining the ct ratio

relay = {
    'R1': [2.431, 1.264],
    'R2': [1.052],
    'R3': [1.264, 0.491, 0.708, 0.698],
    'R4': [1.998, 1.052],
    'R5': [2.08, 1.08],
    'R6': [1.247, 0.679, 0.707, 0.371],
    'R7': [1.08, 0.371],
    'R8': [2.403, 1.247],
    'R9': [1.596, 0.864, 0.83, 0.6],
    'R10': [1.831],
    'R11': [2.398, 1.3],
    'R12': [1.129, 0.199],
    'R13': [1.3, 0.762, 0.772, 0.489],
    'R14': [2.063, 1.129],
}

CTR = {}

def choose_relay(relay_number, relay, CTR):
    fault = relay # array of fault current through a relay
    fault.sort() # sorting the fault current from minimum to maximum
    Isc = fault[0] # 1st value is the minimum current after sorting
    standard_relay = [1200/5, 1000/5, 900/5, 800/5, 600/5, 500/5, 150/5, 50/5 ] # relays used in our paper

    for i in standard_relay:

        try:
            trip = tripping_time(Isc, i)
            if(trip > 0):
                print("'{}': {}/5,".format(relay_number,int(i*5)))
                CTR[relay_number] = i / 5 # populating the CT dictionary CT = {'R1': 200,...}
                break 
            else:
                pass
        except ZeroDivisionError:
            pass

for individual_relay in relay.keys():
    choose_relay(individual_relay, relay[individual_relay], CTR)

def ct_ratio():
    return CTR
