#!/usr/bin/python3
# -*-coding: utf-8 -*

import Simulator.DIPMSimulator as DipmSim
import Simulator.SCPMSimulator as ScpmSim
import tools.Archivist as Archivist
from tools import Tools


class GaSimulator:
    @staticmethod
    def run_sims(model: str, conf: {}) -> [str]:
        sim = None
        results = []
        for i in range(0, 121):
            if model == 'dipm':
                sim = DipmSim.DIPMSimulator()
            elif model == 'scpm':
                sim = ScpmSim.SCPMSimulator()

            exp = Tools.normalized_number(3, i)
            result = 'results/exp2/' + 'results_' + model + '_exp2_' + exp + '.p'
            results.append(result)

            sim.init_with_config(conf)
            sim.run_sim(result)

            return results

    @staticmethod
    def analyze_results(filenames: [str], conf: {}) -> {}:
        results = {}
        channels = conf['channels']
        salience = conf['salience']
        dt = conf['dt']
        val = {}
        for sim_number in range(0, len(filenames)):  # for each simulation
            data = Archivist.load(filenames[sim_number])
            gpi_outputs = data['gpi_outputs']
            channel_res = {}
            for channel in range(0, channels):  # for each channel
                tmp = []
                salience_res = {}
                for s in range(0, len(salience[channel])):  # for each salience 0.0, 0.1, ..., 1.0 of channel channel
                    time_intervals = int(1/dt)
                    for i in range(0, time_intervals):  # for each dt of salience s
                        tmp.append(gpi_outputs[channel][i + s * time_intervals])  # append outputs of gpi to tmp
                    avg = sum(tmp) / len(tmp)   # we average the whole interval
                    val = salience_res.get(salience[channel][s], [])
                    val.append(avg)
                    salience_res.update({salience[channel][s]: val})
                channel_res.update({channel: salience_res})
            val.update({sim_number: channel_res})
    
        chan_tmp = {}
        for exp in val.keys():
            for channel in val[exp]:
                sal_tmp = {}
                for sal in val[exp][channel]:
                    tmp = sal_tmp.get(sal, [])
                    for value in val[exp][channel][sal]:
                        tmp.append(value)
                    sal_tmp.update({sal: tmp})
                chan_tmp.update({channel: sal_tmp})

        results = {}
        for channel in results.keys():
            sal = results.get(channel, {})
            for s in results[channel]:
                res = sum(results[channel][s]) / len(results[channel][s])
                sal.update({s: res})
            results.update({channel: sal})

        return results
