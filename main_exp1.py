#!/usr/bin/python3
# -*-coding: utf-8 -*

from tools import Tools
from tools.Configs import ConfigExp1
import tools.Display as Display
import tools.Archivist as Archivist
import Simulator.DIPMSimulator as DipmSim
import Simulator.SCPMSimulator as ScpmSim
from tools.individuals.loader import Loader
from tools.individuals.Individuals import GaDipmFifths, GaScpmFifths, GaScpmTenths

"""
This is the main to launch to get the results of experience one of the paper called 
"Biology inspired robot behaviour selection mechanism", 2007, by Wang et al.
The exported figures correspond to figure 3 in the paper. 
"""
def exp1():
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


def exp1_param_ga():
    sim = None

    models = ['dipm', 'scpm']

    for model in models:
        individual = []
        data = []

        conf = {}
        model_conf = {}
        if model == 'dipm':
            sim = DipmSim.DIPMSimulator()
            conf = ConfigExp1.config_dipm_exp1_3_channels()
            # model, threshold, fitness_value, data, individual = Loader.load_individual('mat_dipm_11.txt')
            individual = GaDipmFifths.FIT_29_GEN5_401.value
            data = GaDipmFifths.data.value
        elif model == 'scpm':
            sim = ScpmSim.SCPMSimulator()
            conf = ConfigExp1.config_scpm_exp1_3_channels()
            individual = GaScpmTenths.FIT_121_GEN_4891.value
            data = GaScpmTenths.data.value

        # we update the model's weights' configuration
        model_conf = Tools.update_conf(model_conf, data, individual)
        # we update the sim's configuration
        conf.update({'model_conf': {0: model_conf, 1: model_conf, 2: model_conf}})
        # config = None
        results = 'results/results_' + model + '_exp1_param2.p'
        export = 'img_export/' + model + '_exp1_param2'


        for i in range(1, 4):
            individual[-i] = -individual[-i]

        sim.init_with_config(conf)
        sim.run_sim(results)
        data = Archivist.load(results)

        Display.display_all_and_save(data['gpi_outputs'], model, export, [0, 1, 2], data['salience'], 0.05)
        # Display.display_all_and_save(data['gpi_outputs'], model, export, [0, 1, 2, 3, 4, 5], data['salience'], 0.05)

exp1_param_ga()