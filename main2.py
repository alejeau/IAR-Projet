#!/usr/bin/python3
# -*-coding: utf-8 -*

import Simulator.DIPMSimulator as DipmSim
import Simulator.SCPMSimulator as ScpmSim
import tools.Archivist as Archivist
import tools.Display as Display

sim = None
models = ['dipm', 'scpm']

def conf_gen():
    conf = {}

    # activation
    conf.update({'a_d1': 0.2})
    conf.update({'a_d2': 0.2})
    conf.update({'a_gpe': 0.2})
    conf.update({'a_stn': 0.2})
    conf.update({'a_gpi': 0.2})

    # weights
    conf.update({'wcs1': 1.0})
    conf.update({'wcs2': 1.0})
    conf.update({'wsd2_gpe': 1.0})
    conf.update({'wgpe_stn': 1.0})
    conf.update({'wsd1_gpi': 1.0})
    conf.update({'stn_gpi': 1.0})

    # threshold
    conf.update({'theta_d1': 0.2})
    conf.update({'theta_d2': 0.2})
    conf.update({'theta_gpe': -0.2})
    conf.update({'theta_stn': -0.25})
    conf.update({'theta_gpi': -0.2})

    # slope parameter
    conf.update({'m': 1.0})
    # activation rate
    conf.update({'k': 25.0})
    # time increment
    conf.update({'dt': 1.0})

    conf.update({'y_d1': 0.0})
    conf.update({'y_d2': 0.0})
    conf.update({'y_gpe': 0.0})
    conf.update({'y_stn': 0.0})
    conf.update({'y_gpi': 0.0})

    return conf


def config_dipm_exp1():
    config = {}
    name = 'dipm1'
    model_conf = {
        0: None,
        1: None,
        2: None
    }
    nb_of_runs = 5
    time_interval = 1.0
    channels = 3
    dt = 0.001
    salience = {
        0: [0.0, 0.4, 0.4, 0.6, 0.4],
        1: [0.0, 0.0, 0.6, 0.6, 0.6],
        2: [0.0 for i in range(0, nb_of_runs)]
    }

    config.update({'name': name})
    config.update({'model_conf': model_conf})
    config.update({'nb_of_runs': nb_of_runs})
    config.update({'time_interval': time_interval})
    config.update({'channels': channels})
    config.update({'salience': salience})
    config.update({'dt': dt})

    return config


points = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
confs = []
for wsd2_gpe in points:
    for wgpe_stn in points:
        for wsd1_gpi in points:
            for wstn_gpi in points:
                conf = conf_gen()
                conf.update({'wsd2_gpe': wsd2_gpe})
                conf.update({'wgpe_stn': wgpe_stn})
                conf.update({'wsd1_gpi': wsd1_gpi})
                conf.update({'wstn_gpi': wstn_gpi})
                conf_name = 'dipm' + '_' + str(wsd2_gpe) + '_' + str(wgpe_stn) + '_' + str(wsd1_gpi) + '_' + str(wstn_gpi)
                confs.append(conf_name)
                sim_conf = config_dipm_exp1()
                sim_conf.update({'model_conf': {0: conf, 1: conf, 2: conf}})
                sim = DipmSim.DIPMSimulator()
                sim.init_from_config(sim_conf)
                config = 'configs/test/' + conf_name + '.p'
                results = 'results/' + conf_name + '.p'
                export = 'img_export/' + conf_name + '.png'
                print('Executing ' + conf_name + '...')
                sim.run_sim(results)
                data = Archivist.load(results)
                print('Saving ' + conf_name + '...')
                Display.display_and_save(data['gpi_outputs'], 'dipm', export, [0, 1, 2])