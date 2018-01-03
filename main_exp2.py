#!/usr/bin/python3
# -*-coding: utf-8 -*

import Simulator.DIPMSimulator as DipmSim
import Simulator.SCPMSimulator as ScpmSim
import tools.Archivist as Archivist
import tools.Display as Display
import tools.Configs.ConfigExp2 as Config
import models.AbilitiesMatrix as AbilitiesMatrix


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


def run_improved_sims():
    sim = None
    models = ['dipm', 'scpm']

    for model in models:
        if model == 'dipm':
            conf = Config.improved_config_dipm_exp2()
        else:
            conf = Config.improved_config_scpm_exp2()

        for i in range(0, 121):
            if model == 'dipm':
                sim = DipmSim.DIPMSimulator()
            elif model == 'scpm':
                sim = ScpmSim.SCPMSimulator()

            filename_ending = normalized_number(3, i) + '.p'
            results = 'results/exp2/' + 'results_improved_' + model + '_exp2_' + filename_ending

            sim.init_with_config(conf)
            sim.run_sim(results)


def analyze_results(improved_sim: bool):
    # result: {Model: {channel: {index: value}}}
    # results = {str: {int: {float: float}}}
    results = {}
    channels = Config.config_scpm_exp2()['channels']
    salience = Config.config_scpm_exp2()['salience']
    dt = Config.config_scpm_exp2()['dt']
    improved = 'improved' if improved_sim else ''

    models = ['dipm', 'scpm']

    # model_res: {Model: {sim_number {channel: {salience: [value]}}}}
    model_res = {}
    for model in models:
        for sim_number in range(0, 121):
            filename = 'results/exp2/' + 'results_' + improved + '_' + model + '_exp2_'\
                       + normalized_number(3, sim_number) + '.p'
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
    for model in results.keys():
        title = str(model) + ' exp2'
        export_name = str(model) + '_exp2'
        Display.save_simple(results[model], title, 'img_export/exp2/' + export_name)


def exp2(model: str, improved_sim: bool):
    results = analyze_results(improved_sim)
    display_curves(results)

    matrix = AbilitiesMatrix.AbilitiesMatrix()
    if model is 'dipm':
        matrix.generate_matrix(results['dipm'][0], results['dipm'][1], 0.05)
    elif model is 'scpm':
        matrix.generate_matrix(results['scpm'][0], results['dipm'][1], 0.05)
    Display.save_abilities_figure(matrix, '', '')


def nice_one():
    abscissa = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    values1 = [1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.4, 0.0]
    values2 = [1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.0]
    chan1 = {}
    chan2 = {}
    for i in range(len(abscissa)):
        chan1.update({abscissa[i]: values1[i]})
        chan2.update({abscissa[i]: values2[i]})
    matrix = AbilitiesMatrix.AbilitiesMatrix()
    matrix.generate_matrix(chan1, chan2, 0.3)
    Display.save_abilities_figure(matrix, '', '')


def main():
    # run_sims()
    # run_improved_sims()
    nice_one()
    # exp2('dipm', improved_sim=False)
    # exp2('scpm', improved_sim=False)
    # exp2('dipm', improved_sim=True)
    # exp2('scpm', improved_sim=True)


main()
