#!/usr/bin/python3
# -*-coding: utf-8 -*

import matplotlib.pyplot as plt


def load_file():
    pass


def display_data(gpi_outputs: {int: {int: float}}):
    channels = sorted(gpi_outputs.keys())
    # one empty list per channel
    ordonnees = [[] for i in range(len(channels))]
    # init the fig
    plt.figure(1)
    for channel in channels:
        # max should be len, but we get an error because we do not have all of our points...
        sample_size = max(gpi_outputs[channel].keys())
        scale = int(sample_size / 1000)
        # 1000 per plot max, so we pick only one value out of size/1000
        print(sample_size)
        print(scale)
        abscisses = [i for i in range(0, sample_size, scale)]
        for i in abscisses:
            ordonnees[channel].append(gpi_outputs[channel][i])

        # rows, column, plot number as 31X (3 columns, 1 row, channel X)
        id = 100 + len(channels) * 10 + channel + 1
        plt.subplot(id)
        plt.plot(abscisses, ordonnees[channel])
    plt.show()