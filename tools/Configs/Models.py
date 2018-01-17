#!/usr/bin/python3
# -*-coding: utf-8 -*


def get_dipm_base_generator():
    conf = {}

    # weights
    conf.update({'wcs1': 1.0})
    conf.update({'wcs2': 1.0})
    conf.update({'wsd2_gpe': 1.0})
    conf.update({'wgpe_stn': 1.0})
    conf.update({'wsd1_gpi': 1.0})
    conf.update({'wstn_gpi': 0.8})

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
    conf.update({'dt': 0.001})

    # activation
    conf.update({'a_d1': 0.0})
    conf.update({'a_d2': 0.0})
    conf.update({'a_gpe': 0.0})
    conf.update({'a_stn': 0.0})
    conf.update({'a_gpi': 0.0})

    return conf


def get_scpm_base_generator():
    conf = {}

    # weights
    conf.update({'wcs1': 1.0})
    conf.update({'wcs2': 1.0})
    conf.update({'wsd2_gpe': 1.0})
    conf.update({'wc_stn': 1.0})
    conf.update({'wgpe_stn': 1.0})
    conf.update({'wsd1_gpi': 1.0})
    conf.update({'wstn_gpe': 0.8})
    conf.update({'wstn_gpi': 0.8})
    conf.update({'wgpe_gpi': 0.4})

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
    conf.update({'dt': 0.001})

    # activation
    conf.update({'a_d1': 0.0})
    conf.update({'a_d2': 0.0})
    conf.update({'a_gpe': 0.0})
    conf.update({'a_stn': 0.0})
    conf.update({'a_gpi': 0.0})

    return conf
