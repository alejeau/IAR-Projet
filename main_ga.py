#!/usr/bin/python3
# -*-coding: utf-8 -*

import tools.GA as GA


population_size = 100
generations = 100
crossover_proba = 0.8
mutation_proba = 0.02
elitism = True

models = ['dipm', 'scpm']

for model in models:
    if model == 'dipm':
        dipm_data = ['wcs1', 'wcs2', 'wsd2_gpe', 'wgpe_stn', 'wsd1_gpi', 'wstn_gpi',
                     'theta_d1', 'theta_d2', 'theta_gpe', 'theta_stn', 'theta_gpi']

        GA.run_ga(dipm_data, population_size, generations, crossover_proba, mutation_proba, elitism)

    elif model == 'scpm':
        scpm_data = ['wcs1', 'wcs2', 'wsd2_gpe', 'wc_stn', 'wgpe_stn', 'wsd1_gpi', 'wstn_gpe', 'wstn_gpi', 'wgpe_gpi',
                     'theta_d1', 'theta_d2', 'theta_gpe', 'theta_stn', 'theta_gpi']

        GA.run_ga(scpm_data, population_size, generations, crossover_proba, mutation_proba, elitism)
