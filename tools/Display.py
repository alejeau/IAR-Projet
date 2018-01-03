#!/usr/bin/python3
# -*-coding: utf-8 -*

import matplotlib.pyplot as plt
import models.AbilitiesMatrix as AbilitiesMatrix


def load_file():
    pass


def display_data(gpi_outputs: {int: {int: float}}):
    display_and_save(gpi_outputs, '', '')


def display_and_save(gpi_outputs: {int: {int: float}}, title: str, export_name: str, channels_to_display: [int]):
    channels = sorted(gpi_outputs.keys())
    # one empty list per channel
    ordonnees = [[] for i in range(len(channels_to_display))]
    # init the fig
    fig = plt.figure(figsize=(3*len(channels_to_display), 3), dpi=300)
    for channel in channels:
        if channel in channels_to_display:
            # max should be len, but we get an error because we do not have all of our points...
            sample_size = max(gpi_outputs[channel].keys())
            scale = int(sample_size / 1000)
            # 1000 per plot max, so we pick only one value out of size/1000

            abscisses = [i for i in range(0, sample_size + 1, scale)]
            for i in abscisses:
                ordonnees[channel].append(gpi_outputs[channel][i])

            # rows, column, plot number as 13X (1 row, 3 columns, channel X)
            fig_id = 100 + len(channels_to_display) * 10 + channel + 1
            plt.subplot(fig_id)
            normalized_abcsisses = [a/1000.0 for a in abscisses]
            ax = plt.gca()
            ax.set_title(title + ": channel " + str(channel + 1))
            ax.set_xlim([0, 5])
            ax.set_ylim([0, 1])
            plt.plot(normalized_abcsisses, ordonnees[channel])

    if export_name is not (None or ''):
        plt.savefig(export_name)
    else:
        plt.show()

    plt.close(fig)


def save_simple(gpi_outputs: {int: {float: float}},
                title: str,
                export_name: str):
    channels = sorted(gpi_outputs.keys())
    # one empty list per channel
    ordinates = [[] for i in range(len(channels))]
    # init the fig
    fig = plt.figure(figsize=(3*len(channels), 3), dpi=300)
    for channel in channels:
        abscissae = sorted(gpi_outputs[channel].keys())
        for a in abscissae:
            ordinates[channel].append(gpi_outputs[channel][a])

        # rows, column, plot number as 13X (1 row, 3 columns, channel X)
        fig_id = 100 + len(channels) * 10 + channel + 1
        plt.subplot(fig_id)
        ax = plt.gca()
        ax.set_title(title + ": channel " + str(channel + 1))
        ax.set_xlim([0, 1])
        ax.set_ylim([0, 1])
        plt.plot(abscissae, ordinates[channel])
        lines = plt.plot(abscissae, abscissae)
        plt.setp(lines, color='red')

    if export_name is not (None or ''):
        plt.savefig(export_name)
    else:
        plt.show()

    plt.close(fig)


def display_all_and_save(gpi_outputs: {int: {int or float: float}}, title: str, export_name: str,
                         channels_to_display: [int], saliences: {int: [float]}, selection_threshold: float):
    channels = sorted(gpi_outputs.keys())
    # one empty list per channel
    ordonnees = [[] for i in range(len(channels_to_display))]
    # init the fig
    fig = plt.figure(figsize=(3*len(channels_to_display), 3), dpi=300)
    for channel in channels:
        if channel in channels_to_display:
            # max should be len, but we get an error because we do not have all of our points...
            sample_size = max(gpi_outputs[channel].keys())
            scale = int(sample_size / 1000)
            # 1000 per plot max, so we pick only one value out of size/1000

            abscisses = [i for i in range(0, sample_size + 1, scale)]
            salience = []
            for i in abscisses:
                ordonnees[channel].append(gpi_outputs[channel][i])
                salience.append(saliences[channel][int(i / 1000)])

            # rows, column, plot number as 13X (1 row, 3 columns, channel X)
            fig_id = 100 + len(channels_to_display) * 10 + channel + 1
            plt.subplot(fig_id)
            normalized_abcsisses = [a/1000.0 for a in abscisses]
            ax = plt.gca()
            ax.set_title(title + ": channel " + str(channel + 1))
            ax.set_xlim([0, 5])
            ax.set_ylim([0, 1])
            plt.plot(normalized_abcsisses, ordonnees[channel])
            lines = plt.plot(normalized_abcsisses, salience)
            plt.setp(lines, color='red')
            lines = plt.plot([0.0, 5.0], [selection_threshold, selection_threshold])
            plt.setp(lines, color='green')

    if export_name is not (None or ''):
        plt.savefig(export_name)
    else:
        plt.show()

    plt.close(fig)


def flexible_display_or_save(gpi_outputs: {int: {int or float: float}},
                             title: str,
                             export_name: str,
                             channels_to_display: [int],
                             saliences: {int: [float]},
                             selection_threshold: float):
    channels = sorted(gpi_outputs.keys())
    # one empty list per channel
    ordonnees = [[] for i in range(len(channels_to_display))]
    # init the fig
    fig = plt.figure(figsize=(3*len(channels_to_display), 3), dpi=300)
    for channel in channels:
        if channel in channels_to_display:
            x_lim = len(saliences[0])
            # max should be len, but we get an error because we do not have all of our points...
            sample_size = max(gpi_outputs[channel].keys())
            scale = int(sample_size / 1000)
            # 1000 per plot max, so we pick only one value out of size/1000

            abscisses = [i for i in range(0, sample_size + 1, scale)]
            salience = []
            for i in abscisses:
                ordonnees[channel].append(gpi_outputs[channel][i])
                salience.append(saliences[channel][int(i / 1000)])

            # rows, column, plot number as 13X (1 row, 3 columns, channel X)
            fig_id = 100 + len(channels_to_display) * 10 + channel + 1
            plt.subplot(fig_id)
            normalized_abcsisses = [a/1000.0 for a in abscisses]
            ax = plt.gca()
            ax.set_title(title + ": channel " + str(channel + 1))
            ax.set_xlim([0, x_lim])
            ax.set_ylim([0, 1])
            plt.plot(normalized_abcsisses, ordonnees[channel])
            lines = plt.plot(normalized_abcsisses, salience)
            plt.setp(lines, color='red')
            lines = plt.plot([0.0, x_lim], [selection_threshold, selection_threshold])
            plt.setp(lines, color='green')

    if export_name is not (None or ''):
        plt.savefig(export_name)
    else:
        plt.show()

    plt.close(fig)


def save_abilities_figure(abilities_matrix: AbilitiesMatrix):
    pass
