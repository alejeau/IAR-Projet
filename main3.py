#!/usr/bin/python3
# -*-coding: utf-8 -*

import Simulator.DIPMSimulator as DipmSim
import Simulator.SCPMSimulator as ScpmSim
import tools.Archivist as Archivist
import tools.Display as Display


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


conf = conf_gen()
# conf.update({'wcs1': 1.3})
# conf.update({'wcs2': 1.3})
conf.update({'wsd2_gpe': 0.35})
# conf.update({'wgpe_stn': 1.0})
# conf.update({'wsd1_gpi': 1.0})
# conf.update({'stn_gpi': 1.0})
conf_name = 'dipm' + '_' + str(conf['wcs1']) + '_' + str(conf['wcs2']) + '_' + str(conf['wsd2_gpe']) + '_' + str(conf['wgpe_stn']) + '_' + str(conf['wsd1_gpi']) + '_' + str(conf['stn_gpi'])
sim_conf = config_dipm_exp1()
sim_conf.update({'model_conf': {0: conf, 1: conf, 2: conf}})
sim = DipmSim.DIPMSimulator()
sim.init_from_config(sim_conf)
config = 'configs/sim2/' + conf_name + '.p'
results = 'results/sim2/' + conf_name + '.p'
export = 'img_export/sim2/' + conf_name + '.png'
print('Executing ' + conf_name + '...')
sim.run_sim(results)
data = Archivist.load(results)
print('Saving ' + conf_name + '...')

Display.display_and_save(data['gpi_outputs'], 'dipm', export, [0, 1, 2])
