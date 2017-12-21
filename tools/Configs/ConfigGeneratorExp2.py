#!/usr/bin/python3
# -*-coding: utf-8 -*

import tools.Archivist as Archivist


def config_dipm_exp2() -> {}:
    conf = {}
    name = 'dipm2'
    model_conf = {
        0: None,
        1: None,
    }
    salience = {
        0: [0.0, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.0],
        1: [0.0, 0.0, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
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


def config_scpm_exp2() -> {}:
    conf = {}
    name = 'scpm2'
    model_conf = {
        0: None,
        1: None,
    }
    salience = {
        0: [0.0, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.0],
        1: [0.0, 0.0, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
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


Archivist.store(config_dipm_exp2(), '../../configs/config_dipm_exp2.p')
Archivist.store(config_scpm_exp2(), '../../configs/config_scpm_exp2.p')
