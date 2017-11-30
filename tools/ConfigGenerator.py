#!/usr/bin/python3
# -*-coding: utf-8 -*

import pickle


def config1_generator():
    config1 = {}
    name = 'sim1'
    nb_of_runs = 5
    time_interval = 1.0
    channels = 3
    salience = {
        0: [0.0, 0.4, 0.4, 0.6, 0.4],
        1: [0.0, 0.0, 0.6, 0.6, 0.6],
        2: [0.0 for i in range(0, 5)]
    }

    config1.update({'name': name})
    config1.update({'nb_of_runs': nb_of_runs})
    config1.update({'time_interval': time_interval})
    config1.update({'channels': channels})
    config1.update({'salience': salience})


def serialize_config(config: dict, file_name: str):
    # Using pickle's serialization to keep int keys as int
    with open(file_name, 'wb') as results_file:
        pickle.dump(config, results_file)
    results_file.close()



