#!/usr/bin/python3
# -*-coding: utf-8 -*

from tools.Configs import ConfigExp1
import tools.Display as Display
import tools.Archivist as Archivist
import Simulator.DIPMSimulator as DipmSim
import Simulator.SCPMSimulator as ScpmSim

"""
This is the main to launch to get the results of experience one of the paper called 
"Biology inspired robot behaviour selection mechanism", 2007, by Wang et al.
The exported figures correspond to figure 3 in the paper. 
"""

sim = None

models = ['dipm', 'scpm']

for model in models:
    config = None
    results = 'results/results_' + model + '_exp1.p'
    export = 'img_export/' + model + '_exp1'

    if model == 'dipm':
        sim = DipmSim.DIPMSimulator()
        config = ConfigExp1.config_dipm_exp1_3_channels()
    elif model == 'scpm':
        sim = ScpmSim.SCPMSimulator()
        config = ConfigExp1.config_scpm_exp1_3_channels()

    sim.init_with_config(config)
    sim.run_sim(results)
    data = Archivist.load(results)

    Display.display_all_and_save(data['gpi_outputs'], model, export, [0, 1, 2], data['salience'], 0.05)
    # Display.display_all_and_save(data['gpi_outputs'], model, export, [0, 1, 2, 3, 4, 5], data['salience'], 0.05)
