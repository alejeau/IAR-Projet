#!/usr/bin/python3
# -*-coding: utf-8 -*

import Simulator.DIPMSimulator as DipmSim
import Simulator.SCPMSimulator as ScpmSim
import tools.Archivist as Archivist
import tools.Display as Display
import tools.Configs.ConfigExp2 as Config
import models.matrix.AbilitiesMatrix as AbilitiesMatrix
from tools.Configs.Matrices.GoalMatrices import GoalMatrices


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

            exp = normalized_number(3, i)
            results = 'results/exp2/' + 'results_' + model + '_exp2_' + exp + '.p'

            sim.init_with_config(conf)
            sim.run_sim(results)
            # data = Archivist.load(results)
            # export_file = 'img_export/exp2/multi/' + model + '_exp2_' + exp + '.png'
            # Display.flexible_display_or_save(data['gpi_outputs'], model, export_file, [0, 1], data['salience'], 0.05)


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

            exp = normalized_number(3, i)
            results = 'results/exp2/' + 'results_improved_' + model + '_exp2_' + exp + '.p'

            sim.init_with_config(conf)
            sim.run_sim(results)
            # data = Archivist.load(results)
            # export_file = 'img_export/exp2/multi/improved_' + model + '_exp2_' + exp + '.png'
            # Display.flexible_display_or_save(data['gpi_outputs'], model, export_file, [0, 1], data['salience'], 0.05)


def analyze_results(improved_sim: bool):
    # result: {Model: {channel: {index: value}}}
    # results = {str: {int: {float: float}}}
    results = {}
    channels = Config.config_scpm_exp2()['channels']
    salience = Config.config_scpm_exp2()['salience']
    dt = Config.config_scpm_exp2()['dt']
    improved = 'improved_' if improved_sim else ''

    models = ['dipm', 'scpm']

    # model_res: {Model: {sim_number {channel: {salience: [value]}}}}
    model_res = {}
    for model in models:  # for each model
        for sim_number in range(0, 121):  # for each simulation
            filename = 'results/exp2/' + 'results_' + improved + model + '_exp2_' + normalized_number(3, sim_number) + '.p'
            data = Archivist.load(filename)
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
            val = model_res.get(model, {})
            val.update({sim_number: channel_res})
            model_res.update({model: val})

    # Archivist.pretty_store(model_res, 'results/model_res.txt')

    res_tmp = {}
    for model in models:
        chan_tmp = {}
        for exp in model_res[model]:
            for channel in model_res[model][exp]:
                sal_tmp = {}
                for sal in model_res[model][exp][channel]:
                    tmp = sal_tmp.get(sal, [])
                    for value in model_res[model][exp][channel][sal]:
                        tmp.append(value)
                    sal_tmp.update({sal: tmp})
                chan_tmp.update({channel: sal_tmp})
            res_tmp.update({model: chan_tmp})

    # Archivist.pretty_store(res_tmp, 'results/res_tmp.txt')

    for model in models:
        chan = results.get(model, {})
        for channel in res_tmp[model]:
            sal = chan.get(channel, {})
            for s in res_tmp[model][channel]:
                res = sum(res_tmp[model][channel][s]) / len(res_tmp[model][channel][s])
                sal.update({s: res})
            chan.update({channel: sal})
        results.update({model: chan})

    # Archivist.pretty_store(results, 'results/results.txt')

    return results


def display_curves(results):
    for model in results.keys():
        title = str(model) + ' exp2'
        export_name = str(model) + '_exp2'
        Display.save_simple(results[model], title, 'img_export/exp2/' + export_name)


def exp2(model: str, improved_sim: bool, export_name: str):
    results = analyze_results(improved_sim)
    display_curves(results)

    matrix = AbilitiesMatrix.AbilitiesMatrix()
    if model is 'dipm':
        # matrix.generate_matrix(results['dipm'][0], results['dipm'][1], 0.05)
        matrix.generate_matrix(results['dipm'][0], results['dipm'][1], 0.3)
        Display.save_simple_abilities_matrix(matrix.get_matrix(), '', '')
    elif model is 'scpm':
        # matrix.generate_matrix(results['scpm'][0], results['dipm'][1], 0.05)
        matrix.generate_matrix(results['scpm'][0], results['dipm'][1], 0.14)
    Display.save_abilities_figure(matrix, '', export_name)


def nice_one():
    abscissa = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    values1 = [1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.5, 0.0]
    values2 = [1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.4, 0.2, 0.1, 0.0]
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
    # nice_one()
    exp2('dipm', improved_sim=False, export_name="img_export/exp2/dipm_abilities_matrix.png")
    # exp2('scpm', improved_sim=False, export_name="img_export/exp2/scpm_abilities_matrix.png")
    # exp2('dipm', improved_sim=True, export_name="img_export/exp2/dipm_improved_abilities_matrix.png")
    # exp2('scpm', improved_sim=True, export_name="img_export/exp2/scpm_improved_abilities_matrix.png")
    # GoalMatrices.dipm().pprint()
    # Display.save_simple_abilities_matrix(GoalMatrices.dipm(), '', '')
    # GoalMatrices.scpm().pprint()
    # Display.save_simple_abilities_matrix(GoalMatrices.scpm(), '', '')
    pass


main()
