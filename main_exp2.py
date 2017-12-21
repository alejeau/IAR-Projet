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


def main():
    sim = None
    # model = 'dipm'
    # model = 'scpm'

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

            # # Before launching data saving as images, we need the tools to analyze the outputs and generate the right map
            # data = Archivist.load(results)
            # export = 'img_export/' + model + '_exp2' + filename_ending
            # Display.display_all_and_save(data['gpi_outputs'], model, export, [0, 1, 2], data['salience'], 0.05)

main()