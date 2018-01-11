#!/usr/bin/python3
# -*-coding: utf-8 -*

import Simulator.DIPMSimulator as DipmSim
import Simulator.SCPMSimulator as ScpmSim


class GaSimulator:
    @staticmethod
    def run_sims(model: str, conf: {}, number_of_sims: int) -> [str]:
        sim = None
        results = []
        for i in range(number_of_sims):
            if model == 'dipm':
                sim = DipmSim.DIPMSimulator()
            elif model == 'scpm':
                sim = ScpmSim.SCPMSimulator()

            sim.init_with_config(conf)
            res = sim.run_sim('')
            results.append(res)

        return results

    @staticmethod
    def analyze_results(raw_results: [{}], conf: {}, number_of_sims: int) -> {}:
        channels = conf['channels']
        salience = conf['salience']
        dt = conf['dt']
        raw = {}
        for sim_number in range(number_of_sims):  # for each simulation
            data = raw_results[sim_number]
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
            raw.update({sim_number: channel_res})

        chan_tmp = {}
        for exp in raw.keys():
            for channel in raw[exp]:
                sal_tmp = {}
                for sal in raw[exp][channel]:
                    tmp = sal_tmp.get(sal, [])
                    for value in raw[exp][channel][sal]:
                        tmp.append(value)
                    sal_tmp.update({sal: tmp})
                chan_tmp.update({channel: sal_tmp})

        results = {}
        for channel in chan_tmp.keys():
            sal = results.get(channel, {})
            for s in chan_tmp[channel]:
                res = sum(chan_tmp[channel][s]) / len(chan_tmp[channel][s])
                sal.update({s: res})
            results.update({channel: sal})

        return results
