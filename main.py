#!/usr/bin/python3
# -*-coding: utf-8 -*

import Simulator.DIPMSimulator as DipmSim
import Simulator.SCPMSimulator as ScpmSim
import tools.Archivist as Archivist
import tools.Display as Display

sim = None
# model = 'dipm'
# # model = 'scpm'

models = ['dipm', 'scpm']

for model in models:
    config = 'configs/'
    results = 'results/'
    export = 'img_export/'
    if model == 'dipm':
        sim = DipmSim.DIPMSimulator()
        config += 'config_dipm_exp1.p'
        results += 'results_dipm_exp1.p'
        export += model + '_exp1'
    elif model == 'scpm':
        sim = ScpmSim.SCPMSimulator()
        config += 'config_scpm_exp1.p'
        results += 'results_scpm_exp1.p'
        export += model + '_exp1'

    sim.init_and_load_config(config)
    sim.run_sim(results)
    data = Archivist.load(results)

    # print('\nsalience:')
    # keys = sorted(data['salience'].keys())
    # for k in keys:
    #     print(str(k) + ': ' + str(data['salience'][k]))
    #
    # print('\ngpi_outputs:')
    # keys = sorted(data['gpi_outputs'].keys())
    # print('keys: ' + str(keys))
    # for k in keys:
    #     print(str(k) + ': ' + str(data['gpi_outputs'][k]))

    Display.display_all_and_save(data['gpi_outputs'], model, export, [0, 1, 2], data['salience'], 0.05)
