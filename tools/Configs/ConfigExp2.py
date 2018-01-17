#!/usr/bin/python3
# -*-coding: utf-8 -*


def config_dipm_exp2() -> {}:
    conf = {}
    name = 'dipm2'
    model_conf = {
        0: None,
        1: None,
    }
    channels = 2
    nb_of_runs = 6
    time_interval = 1
    dt = 0.001

    conf.update({'name': name})
    conf.update({'model_conf': model_conf})
    conf.update({'nb_of_runs': nb_of_runs})
    conf.update({'time_interval': time_interval})
    conf.update({'channels': channels})
    conf.update({'dt': dt})

    return conf


def config_scpm_exp2() -> {}:
    conf = {}
    name = 'scpm2'
    model_conf = {
        0: None,
        1: None,
    }
    channels = 2
    nb_of_runs = 6
    time_interval = 1
    dt = 0.001

    conf.update({'name': name})
    conf.update({'model_conf': model_conf})
    conf.update({'nb_of_runs': nb_of_runs})
    conf.update({'time_interval': time_interval})
    conf.update({'channels': channels})
    conf.update({'dt': dt})

    return conf
