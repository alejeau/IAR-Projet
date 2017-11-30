#!/usr/bin/python3
# -*-coding: utf-8 -*

import models.DIPM as DIPM
import tools.Archivist as Archivist
import numpy as np


class DIPMSimulator:
    def __init__(self):
        self.dipms = {}
        self.config = None
        self.gpi_output = []
        self.timeline = []

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
        stop = self.config['runs'] * self.config['time_interval']
        self.timeline = np.arange(0, stop, self.config['time_interval'])

    def run_sim(self, result_file: str):
        channels = self.config['channels']
        salience = self.config['salience']
        gpi_outputs = {}

        # main loop of the simulation
        for t in self.timeline:
            for channel in range(0, channels):
                # we get the next result
                res = self.dipms[channel].next(salience[channel][t])
                # we store it
                new = gpi_outputs.get(channel, {})
                new.update({t: res})
                gpi_outputs.update({channel: new})
                pass
        pass

        # once the sim finished, store the results
        Archivist.store(gpi_outputs, result_file)
