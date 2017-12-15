#!/usr/bin/python3
# -*-coding: utf-8 -*

import matplotlib.pyplot as plt

def load_file():
    pass

def display_data(gpi_outputs: {int: {int: float}}):
    print(gpi_outputs)
    abscisses = range(5000, 5)
    ordonnees = [[], [],[]]
    for channel in sorted(gpi_outputs.keys()):
        for i in abscisses:
            ordonnees[channel].append(gpi_outputs[channel][i])


        plt.subplot(131)
        plt.plot(abscisses, ordonnees[channel])
        plt.show()