#!/usr/bin/python3
# -*-coding: utf-8 -*

import Simulator.DIPMSimulator as DipmSim
import Simulator.SCPMSimulator as ScpmSim
import tools.Archivist as Archivist
import tools.display as Display

# sim = DipmSim.DIPMSimulator()
# sim.init_and_load_config('configs/sim1.p')
# sim.run_sim('results/results_sim_1.p')
#
# data = Archivist.load('results/results_sim_1.p')

sim = ScpmSim.SCPMSimulator()
sim.init_and_load_config('configs/sim2.p')
sim.run_sim('results/results_sim_2.p')

data = Archivist.load('results/results_sim_2.p')


print('\nsalience:')
keys = sorted(data['salience'].keys())
for k in keys:
    print(str(k) + ': ' + str(data['salience'][k]))

print('\ngpi_outputs:')
keys = sorted(data['gpi_outputs'].keys())
print('keys: ' + str(keys))
for k in keys:
    print(str(k) + ': ' + str(data['gpi_outputs'][k]))

Display.display_data(data['gpi_outputs'])
