#!/usr/bin/python3
# -*-coding: utf-8 -*

import Simulator.DIPMSimulator as DipmSim
import Simulator.SCPMSimulator as ScpmSim
import tools.Archivist as Archivist
import tools.Display as Display

sim = None
# model = 'dipm'
model = 'scpm'
config = 'configs/'
results = 'results/'
export = 'img_export/'

if model == 'dipm':
    sim = DipmSim.DIPMSimulator()
    config += 'sim1.p'
    results += 'results_sim_dipm.p'
    export += model + '_sim'
elif model == 'scpm':
    sim = ScpmSim.SCPMSimulator()
    config += 'sim2.p'
    results += 'results_sim_scpm.p'
    export += model + '_sim'

sim.init_and_load_config(config)
sim.run_sim(results)
data = Archivist.load(results)

print('\nsalience:')
keys = sorted(data['salience'].keys())
for k in keys:
    print(str(k) + ': ' + str(data['salience'][k]))

print('\ngpi_outputs:')
keys = sorted(data['gpi_outputs'].keys())
print('keys: ' + str(keys))
for k in keys:
    print(str(k) + ': ' + str(data['gpi_outputs'][k]))

Display.display_and_save(data['gpi_outputs'], model, export, [0, 1, 2])
