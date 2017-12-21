#!/usr/bin/python3
# -*-coding: utf-8 -*


def config_dipm_exp1():
    conf = {}
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

    conf.update({'name': name})
    conf.update({'model_conf': model_conf})
    conf.update({'nb_of_runs': nb_of_runs})
    conf.update({'time_interval': time_interval})
    conf.update({'channels': channels})
    conf.update({'salience': salience})
    conf.update({'dt': dt})

    return conf


def config_scpm_exp1():
    conf = {}
    name = 'scpm1'
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

    conf.update({'name': name})
    conf.update({'model_conf': model_conf})
    conf.update({'nb_of_runs': nb_of_runs})
    conf.update({'time_interval': time_interval})
    conf.update({'channels': channels})
    conf.update({'salience': salience})
    conf.update({'dt': dt})

    return conf
