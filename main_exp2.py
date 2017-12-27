#!/usr/bin/python3
# -*-coding: utf-8 -*

import Simulator.DIPMSimulator as DipmSim
import Simulator.SCPMSimulator as ScpmSim
import tools.Archivist as Archivist
import tools.Display as Display
import tools.Configs.ConfigExp2 as Config


def normalized_number(size: int, number: int) -> str:
    n = str(number)
    tmp = ''
    s = size - len(n)
    for i in range(0, s):
        tmp += '0'

    return tmp + n


def run_sims():
    sim = None
    models = ['dipm', 'scpm']

    for model in models:
        if model == 'dipm':
            conf = Config.config_dipm_exp2()
        else:
            conf = Config.config_scpm_exp2()

        for i in range(0, 121):
            if model == 'dipm':
                sim = DipmSim.DIPMSimulator()
            elif model == 'scpm':
                sim = ScpmSim.SCPMSimulator()

            filename_ending = normalized_number(3, i) + '.p'
            results = 'results/exp2/' + 'results_' + model + '_exp2_' + filename_ending

            sim.init_with_config(conf)
            sim.run_sim(results)


def analyze_results():
    # result: {Model: {channel: {index: value}}}
    # results = {str: {int: {float: float}}}
    results = {}
    channels = Config.config_scpm_exp2()['channels']
    salience = Config.config_scpm_exp2()['salience']
    dt = Config.config_scpm_exp2()['dt']

    models = ['dipm', 'scpm']

    # model_res: {Model: {sim_number {channel: {salience: [value]}}}}
    model_res = {}
    for model in models:
        for sim_number in range(0, 121):
            filename = 'results/exp2/' + 'results_' + model + '_exp2_' + normalized_number(3, sim_number) + '.p'
            data = Archivist.load(filename)
            gpi_outputs = data['gpi_outputs']
            channel_res = {}
            for channel in range(0, channels):
                tmp = []
                salience_res = {}
                for s in range(0, len(salience[channel])):
                    for i in range(0, int(1/dt)):
                        tmp.append(gpi_outputs[channel][i + s * (1/dt)])
                    avg = sum(tmp) / len(tmp)
                    val = salience_res.get(salience[channel][s], [])
                    val.append(avg)
                    salience_res.update({salience[channel][s]: val})
                channel_res.update({channel: salience_res})
            val = model_res.get(model, {})
            val.update({sim_number: channel_res})
            model_res.update({model: val})

    Archivist.pretty_store(model_res, 'results/model_res.txt')

    res_tmp = {}
    for model in models:
        chan_tmp = {}
        sal_tmp = {}
        for exp in model_res[model]:
            for channel in model_res[model][exp]:
                for sal in model_res[model][exp][channel]:
                    tmp = sal_tmp.get(sal, [])
                    for value in model_res[model][exp][channel][sal]:
                        tmp.append(value)
                    sal_tmp.update({sal: tmp})
                chan_tmp.update({channel: sal_tmp})
            res_tmp.update({model: chan_tmp})

    Archivist.pretty_store(res_tmp, 'results/res_tmp.txt')

    for model in models:
        chan = results.get(model, {})
        for channel in res_tmp[model]:
            sal = chan.get(channel, {})
            for s in res_tmp[model][channel]:
                res = sum(res_tmp[model][channel][s]) / len(res_tmp[model][channel][s])
                sal.update({s: res})
            chan.update({channel: sal})
        results.update({model: chan})

    Archivist.pretty_store(results, 'results/results.txt')

    return results


def display_curves(results):
    models = ['dipm', 'scpm']
    channels = Config.config_scpm_exp2()['channels']
    salience = Config.config_scpm_exp2()['salience']

    for model in results.keys():
        title = str(model) + ' exp2'
        export_name = str(model) + '_exp2'
        Display.save_simple(results[model], title, 'img_export/exp2/' + export_name)


def main():
    results = analyze_results()
    display_curves(results)

    # # Before launching data saving as images, we need the tools to analyze the outputs and generate the right map
    # data = Archivist.load(results)
    # export = 'img_export/' + model + '_exp2' + filename_ending
    # Display.display_all_and_save(data['gpi_outputs'], model, export, [0, 1, 2], data['salience'], 0.05)


main()
