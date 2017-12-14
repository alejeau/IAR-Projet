#!/usr/bin/python3
# -*-coding: utf-8 -*

import models.DIPM as DIPM
import tools.Archivist as Archivist
import numpy as np


class DIPMSimulator:
    def __init__(self):
        self.dipms = {float: DIPM.DIPM()}
        self.config = None
        self.gpi_output = {float: {float: float}}
        self.old_stn_list = []

    def init_and_load_config(self, filename: str):
        self.config = Archivist.load(filename)
        channels = self.config['channels']
        dipms_conf = self.config['dipms_conf']
        for i in range(0, channels):
            dipm = DIPM.DIPM()
            # if conf of weights and all, load and add
            if dipms_conf[i] is not None:
                dipm.load_conf(dipms_conf[i])

            # add the DIPM
            self.dipms.update({i: dipm})
        self.old_stn_list = [0.0 for i in range(0, channels)]

    def run_sim(self, result_file: str):
        channels = self.config['channels']
        salience = self.config['salience']
        thresholds = {}
        gpi_outputs = {}

        for channel in range(0, channels):
            thresholds.update({channel: self.dipms[channel].get_theta_gpi()})

        # main loop of the simulation
        for t in range(0, self.config['nb_of_runs']):
            stn_list = []
            for channel in range(0, channels):
                # compute y_stn output for each channel
                stn_list.append(self.dipms[channel].compute_d1_to_stn(salience[channel][t]['y_stn']))

            for channel in range(0, channels):
                # compute y_gpi output for each channel
                res = self.dipms[channel].compute_gpi(stn_list)

                # we store it
                new = gpi_outputs.get(channel, {})
                new.update({t: res})
                gpi_outputs.update({channel: new})

        # once the sim finished, store the results
        simulation = {
            'salience': salience,
            'threshold': thresholds,
            'gpi_outputs': gpi_outputs
        }
        Archivist.store(simulation, result_file)
