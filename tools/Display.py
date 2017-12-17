#!/usr/bin/python3
# -*-coding: utf-8 -*

import matplotlib.pyplot as plt


def load_file():
    pass


def display_data(gpi_outputs: {int: {int: float}}):
    display_and_save(gpi_outputs, '')


def display_and_save(gpi_outputs: {int: {int: float}}, export_name: str):
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

        abscisses = [i for i in range(0, sample_size + 1, scale)]
        for i in abscisses:
            ordonnees[channel].append(gpi_outputs[channel][i])

        # rows, column, plot number as 13X (1 row, 3 columns, channel X)
        fig_id = 100 + len(channels) * 10 + channel + 1
        plt.subplot(fig_id)
        plt.plot(abscisses, ordonnees[channel])

    if export_name is not (None or ''):
        plt.savefig(export_name)
    else:
        plt.show()
