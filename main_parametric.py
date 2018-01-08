#!/usr/bin/python3
# -*-coding: utf-8 -*

import Simulator.DIPMSimulator as DipmSim
import Simulator.SCPMSimulator as ScpmSim
import tools.Archivist as Archivist
import tools.Display as Display
import tools.Configs.ConfigExp2 as Config
import tools.Configs.Models as ModelConf
from models import AbilitiesMatrix


def config_dipm_base() -> {}:
    conf = {}
    name = 'dipm2'
    basic_conf = ModelConf.get_dipm_base_generator()
    model_conf = {
        0: basic_conf,
        1: basic_conf,
    }
    salience = {
        0: [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
        1: [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    }
    channels = len(salience)
    nb_of_runs = len(salience[0])
    time_interval = 0.1
    dt = 0.001

    conf.update({'name': name})
    conf.update({'model_conf': model_conf})
    conf.update({'nb_of_runs': nb_of_runs})
    conf.update({'time_interval': time_interval})
    conf.update({'channels': channels})
    conf.update({'salience': salience})
    conf.update({'dt': dt})

    return conf


sim = None
# model = 'dipm'
# model = 'scpm'

models = ['dipm']  #, 'scpm']
improved_sim = True


for model in models:
    config = None
    results = 'results/'
    export = 'img_export/'

    if model == 'dipm':
        sim = DipmSim.DIPMSimulator()
        config = config_dipm_base()
        # config = Config.improved_config_dipm_exp2()
    elif model == 'scpm':
        sim = DipmSim.DIPMSimulator()
        config = Config.improved_config_scpm_exp2()

    sal = {
        0: [0.3 for i in range(11)],
        1: [0.1 for i in range(11)]
    }
    config.update({'salience': sal})

    results += 'results_improved_' + model + '_exp2.p'
    export += 'improved_' + model + '_exp2'

    sim.init_with_config(config)
    sim.run_sim(results)
    data = Archivist.load(results)

    Display.flexible_display_or_save(data['gpi_outputs'], model, '', [0, 1], data['salience'], 0.25)
