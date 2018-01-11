#!/usr/bin/python3
# -*-coding: utf-8 -*

from models.DIPM import DIPM
import tools.Archivist as Archivist


class DIPMSimulator:
    def __init__(self):
        self.dipms = {int: DIPM}
        self.config = None
        self.gpi_output = {float: {float: float}}
        self.dt = 0.001
        self.old_stn_list = []

    def init_and_load_config(self, filename: str):
        self.init_with_config(Archivist.load(filename))

    def init_with_config(self, conf):
        self.config = conf
        channels = self.config['channels']
        dipms_conf = self.config['model_conf']
        self.dt = self.config['dt']
        for i in range(0, channels):
            dipm = DIPM()
            # if conf of weights and all, load and add
            if dipms_conf[i] is not None:
                dipm.load_conf(dipms_conf[i])
            dipm.set_dt(self.dt)
            # add the DIPM
            self.dipms.update({i: dipm})
        self.old_stn_list = [0.0 for _ in range(0, channels)]

    def init_from_config(self, conf):
        self.config = conf
        channels = self.config['channels']
        dipms_conf = self.config['model_conf']
        self.dt = self.config['dt']
        for i in range(0, channels):
            dipm = DIPM()
            # if conf of weights and all, load and add
            if dipms_conf[i] is not None:
                dipm.load_conf(dipms_conf[i])
            dipm.set_dt(self.dt)
            # add the DIPM
            self.dipms.update({i: dipm})
        self.old_stn_list = [0.0 for i in range(0, channels)]

    def run_sim(self, result_file: str):
        channels = self.config['channels']
        salience = self.config['salience']
        thresholds = {}
        gpi_outputs = {}

        for channel in range(channels):
            thresholds.update({channel: self.dipms[channel].get_theta_gpi()})

        # main loop of the simulation
        for r in range(0, self.config['nb_of_runs']):
            for t in range(0, int(1/self.dt)):
                stn_list = []
                for channel in range(channels):
                    values = self.dipms[channel].compute_d1_to_gpi(salience[channel][r], self.old_stn_list)
                    stn_list.append(values['y_stn'])
                    res = values['y_gpi']

                    # we store it
                    new = gpi_outputs.get(channel, {})
                    new.update({t + r * int(1/self.dt): res})
                    gpi_outputs.update({channel: new})
                # update the old list of stn values
                self.old_stn_list = stn_list

        # once the sim finished, store the results
        simulation = {
            'salience': salience,
            'threshold': thresholds,
            'gpi_outputs': gpi_outputs
        }
        if result_file != '':
            Archivist.store_data(simulation, result_file)
        return simulation
