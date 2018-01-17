#!/usr/bin/python3
# -*-coding: utf-8 -*

from tools import Tools
from tools import Display
from tools.Values import Misc
from tools.Configs import Models
from tools.Configs import ConfigExp2
from GA.GaSimulator import GaSimulator
from tools.Configs.Matrices.GoalMatrix import GoalMatrix
from tools.Configs.Matrices.WangGaOptimizedMatrices import WangGaOptimizedMatrices as Ga_mat


def exp2(model, individual, data, threshold, fifths_or_tenths):
    conf = {}
    model_conf = {}
    if model is 'dipm':
        conf = ConfigExp2.config_dipm_exp2()
        model_conf = Models.get_dipm_base_generator()
    elif model is 'scpm':
        conf = ConfigExp2.config_scpm_exp2()
        model_conf = Models.get_scpm_base_generator()

    # we update the model's weights' configuration
    model_conf = Tools.update_conf(model_conf, data, individual)
    # we update the sim's configuration
    conf.update({'model_conf': {0: model_conf, 1: model_conf}})

    results = GaSimulator.run_sims(model, conf, fifths_or_tenths)
    matrix = GaSimulator.analyze_results(results, conf, threshold, fifths_or_tenths)
    Display.save_simple_abilities_matrix(matrix, '', '')


def main_exp2():
    # models = ['dipm', 'scpm']
    # models = ['dipm']
    models = ['scpm']
    individual = [float]
    threshold = 0.05
    fifths_or_tenths = Misc.FIFTHS
    data = [str]

    for model in models:
        if model == 'dipm':
            data = ['wcs1', 'wcs2', 'wsd2_gpe', 'wgpe_stn', 'wsd1_gpi', 'wstn_gpi', 'theta_d1', 'theta_d2', 'theta_gpe',
                    'theta_stn', 'theta_gpi']
            individual = [0.94948035562892, 0.7247278639644021, 0.7626401017720236, 0.1251507767942246,
                          0.6801936362298814, 0.5330200237697756, 0.007677974913827268, 0.17250093305279468,
                          -0.34178973757684383, -0.1805072944715297, -0.3366105426889202]
        elif model == 'scpm':
            data = ['wcs1', 'wcs2', 'wsd2_gpe', 'wc_stn', 'wgpe_stn', 'wsd1_gpi', 'wstn_gpe', 'wstn_gpi', 'wgpe_gpi',
                    'theta_d1', 'theta_d2', 'theta_gpe', 'theta_stn', 'theta_gpi']
            individual = [0.45860185609965864, 0.5214167323687748, 0.21121036565437545, 0.870081341501728,
                          0.6241650146479159, 0.8268923788309985, 0.14454111807730685, 0.08262191791402207,
                          0.2676369188631271, 0.14994831884579007, 0.4981667707565255, -0.5466515671785532,
                          -0.5652687596782892, -0.16848502608438598]

        exp2(model, individual, data, threshold, fifths_or_tenths)


def main():
    # GoalMatrix.matrix_tenth().pprint()
    # Display.save_simple_abilities_matrix(GoalMatrix.matrix_tenth(), '', '')
    # GoalMatrix.matrix_fifth().pprint()
    # Display.save_simple_abilities_matrix(GoalMatrix.matrix_fifth(), '', '')
    # print('Fitness value of GA-DIPM: ' + str(Tools.value_for_fitness(Ga_mat.dipm(), GoalMatrix.matrix_tenth())))
    # print('Fitness value of GA-SCPM: ' + str(Tools.value_for_fitness(Ga_mat.scpm(), GoalMatrix.matrix_tenth())))

    main_exp2()

    pass


main()
