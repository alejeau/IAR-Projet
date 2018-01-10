#!/usr/bin/python3
# -*-coding: utf-8 -*

import GA.GA as GA


population_size = 100
generations = 100
crossover_proba = 0.8
mutation_proba = 0.02
elitism = True

# models = ['dipm', 'scpm']
models = ['dipm']

for model in models:
    data = [str]
    if model == 'dipm':
        data = ['wcs1', 'wcs2', 'wsd2_gpe', 'wgpe_stn', 'wsd1_gpi', 'wstn_gpi', 'theta_d1', 'theta_d2', 'theta_gpe',
                'theta_stn', 'theta_gpi']

    elif model == 'scpm':
        data = ['wcs1', 'wcs2', 'wsd2_gpe', 'wc_stn', 'wgpe_stn', 'wsd1_gpi', 'wstn_gpe', 'wstn_gpi', 'wgpe_gpi',
                'theta_d1', 'theta_d2', 'theta_gpe', 'theta_stn', 'theta_gpi']

    GA.current_model = model
    result = GA.run_ga(data, population_size, generations, crossover_proba, mutation_proba, elitism)
    print(result)

