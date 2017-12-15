#!/usr/bin/python3
# -*-coding: utf-8 -*

import matplotlib.pyplot as plt

def load_file():
    pass

def display_data(gpi_outputs: {int: {int: float}}):
    print(gpi_outputs)
    ordonnees = [[], [],[]]
    channels = sorted(gpi_outputs.keys())
    for channel in channels:
        sample_size = len(gpi_outputs[channel])
        # scale = sample_size / 1000.0
        abscisses = range(5000, 5)
        for i in abscisses:
            ordonnees[channel].append(gpi_outputs[channel][i])

        plt.plot(abscisses, ordonnees[channel])

        # rows, column, plot number
        id = 100 + len(channels) * 10 + channel+1
        print(id)
        plt.subplot(id)
        plt.show()