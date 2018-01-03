#!/usr/bin/python3
# -*-coding: utf-8 -*

import Simulator.DIPMSimulator as DipmSim
import Simulator.SCPMSimulator as ScpmSim
import tools.Archivist as Archivist
import tools.Display as Display
import tools.Configs.ConfigExp2 as Config

sim = None
# model = 'dipm'
# model = 'scpm'

models = ['dipm', 'scpm']
improved_sim = True

for model in models:
    config = None
    results = 'results/'
    export = 'img_export/'

    if model == 'dipm':
        sim = DipmSim.DIPMSimulator()
        config = Config.improved_config_dipm_exp2()
    elif model == 'scpm':
        sim = DipmSim.DIPMSimulator()
        config = Config.improved_config_scpm_exp2()

    results += 'results_improved_' + model + '_exp2.p'
    export += 'improved_' + model + '_exp2'

    sim.init_with_config(config)
    sim.run_sim(results)
    data = Archivist.load(results)

    Display.flexible_display_or_save(data['gpi_outputs'], model, export, [0, 1], data['salience'], 0.05)
