#!/usr/bin/python3
# -*-coding: utf-8 -*

import tools.Archivist as Archivist


def config_dipm1_generator():
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

    Archivist.store(conf, '../configs/dipm1.p')


def config_sim1_generator():
    config1 = {}
    name = 'sim1'
    dipms_conf = {
        0: None,
        1: None,
        2: None
    }
    nb_of_runs = 6
    time_interval = 1.0
    channels = 3
    salience = {
        0: [0.0, 0.4, 0.4, 0.6, 0.4, 0.4],
        1: [0.0, 0.0, 0.6, 0.6, 0.6, 0.6],
        2: [0.0 for i in range(0, nb_of_runs)]
    }

    config1.update({'name': name})
    config1.update({'dipms_conf': dipms_conf})
    config1.update({'nb_of_runs': nb_of_runs})
    config1.update({'time_interval': time_interval})
    config1.update({'channels': channels})
    config1.update({'salience': salience})

    Archivist.store(config1, '../configs/sim1.p')


config_sim1_generator()
config_dipm1_generator()
