#!/usr/bin/python3
# -*-coding: utf-8 -*

import tools.Configs.Models as ModelConf


def config_dipm_exp2() -> {}:
    conf = {}
    name = 'dipm2'
    basic_conf = ModelConf.get_dipm_base_generator()
    model_conf = {
        0: basic_conf,
        1: basic_conf,
    }
    channels = 2
    nb_of_runs = 6
    time_interval = 0.1
    dt = 0.001

    conf.update({'name': name})
    conf.update({'model_conf': model_conf})
    conf.update({'nb_of_runs': nb_of_runs})
    conf.update({'time_interval': time_interval})
    conf.update({'channels': channels})
    conf.update({'dt': dt})

    return conf


def improved_config_dipm_exp2() -> {}:
    conf = config_dipm_exp2()
    conf.update({'basic_conf': ModelConf.get_dipm_improved_generator()})
    return conf


def config_scpm_exp2() -> {}:
    conf = {}
    name = 'scpm2'
    basic_conf = ModelConf.get_scpm_base_generator()
    model_conf = {
        0: basic_conf,
        1: basic_conf,
    }
    channels = 2
    nb_of_runs = 6
    time_interval = 0.1
    dt = 0.001

    conf.update({'name': name})
    conf.update({'model_conf': model_conf})
    conf.update({'nb_of_runs': nb_of_runs})
    conf.update({'time_interval': time_interval})
    conf.update({'channels': channels})
    conf.update({'dt': dt})

    return conf


def improved_config_scpm_exp2() -> {}:
    conf = config_scpm_exp2()
    conf.update({'basic_conf': ModelConf.get_scpm_improved_generator()})
    return conf
