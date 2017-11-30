#!/usr/bin/python3
# -*-coding: utf-8 -*

import models.DIPM as DIPM
import tools.ConfigurationLoader as confLoader


class DIPMSimulator:
    def __init__(self):
        self.dipms = {}
        self.config = None
        self.gpi_output = []

    def init_and_load_config(self, filename: str):
        self.config = confLoader.load(filename)
        channels = self.config['channels']
        dipms_conf = self.config['dipms_conf']
        for i in range(0, channels):
            dipm = DIPM.DIPM()
            # if conf of weights and all, load and add
            if dipms_conf[i] is not None:
                dipm.load_conf(dipms_conf[i])

            # add the DIPM
            self.dipms.update({i: dipm})

    def run_sim(self):
        pass
