#!/usr/bin/python3
# -*-coding: utf-8 -*

from tools import Tools
from tools import Display
from tools.Values import Misc
from tools.Configs import Models
from tools.Configs import ConfigExp2
from tools.individuals.loader import Loader
from tools.individuals.Individuals import GaDipmFifths, GaScpmFifths, GaScpmTenths
from GA.GaSimulator import GaSimulator
from tools.Configs.Matrices.GoalMatrix import GoalMatrix


def exp2(model, individual, data, threshold, fifths_or_tenths, export_file, title):
    conf = {}
    model_conf = {}
    if model == 'dipm':
        conf = ConfigExp2.config_dipm_exp2()
        model_conf = Models.get_dipm_base_generator()
    elif model == 'scpm':
        conf = ConfigExp2.config_scpm_exp2()
        model_conf = Models.get_scpm_base_generator()

    # we update the model's weights' configuration
    model_conf = Tools.update_conf(model_conf, data, individual)
    # we update the sim's configuration
    conf.update({'model_conf': {0: model_conf, 1: model_conf}})

    results = GaSimulator.run_sims(model, conf, fifths_or_tenths)
    matrix = GaSimulator.analyze_results(results, conf, threshold, fifths_or_tenths)
    goal = GoalMatrix.matrix_fifth() if fifths_or_tenths is Misc.FIFTHS else GoalMatrix.matrix_tenth()
    print('Fitness value: ' + str(Tools.value_for_fitness(matrix, goal)))

    coordinates_fifths = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
    coordinates_tenths = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    coordinates = [coordinates_fifths, coordinates_fifths] if fifths_or_tenths == Misc.FIFTHS else [coordinates_tenths, coordinates_tenths]
    Display.save_simple_abilities_matrix(matrix, title, export_file, coordinates)


def main_exp2():
    # models = ['dipm', 'scpm']
    # models = ['dipm']
    models = ['scpm']
    individual = None
    threshold = 0.05
    fifths_or_tenths = Misc.FIFTHS
    # fifths_or_tenths = Misc.TENTHS
    data = [str]

    for model in models:
        if model == 'dipm':
            data = ['wcs1', 'wcs2', 'wsd2_gpe', 'wgpe_stn', 'wsd1_gpi', 'wstn_gpi', 'theta_d1', 'theta_d2', 'theta_gpe',
                    'theta_stn', 'theta_gpi']
            individual = GaDipmFifths.FIT_29_GEN5_401.value
        elif model == 'scpm':
            data = ['wcs1', 'wcs2', 'wsd2_gpe', 'wc_stn', 'wgpe_stn', 'wsd1_gpi', 'wstn_gpe', 'wstn_gpi', 'wgpe_gpi',
                    'theta_d1', 'theta_d2', 'theta_gpe', 'theta_stn', 'theta_gpi']
            if fifths_or_tenths is Misc.FIFTHS:
                # individual = GaScpmFifths.FIT_36_GEN_211.value
                individual = GaScpmFifths.FIT_36_GEN_442.value
            else:
                # individual = GaScpmTenths.FIT_121_GEN_4290.value
                individual = GaScpmTenths.FIT_121_GEN_4891.value

        export_file = ''
        title = 'GA-' + model.upper() + ', fitness: 121'
        exp2(model, individual, data, threshold, fifths_or_tenths, export_file, title)


def main_exp2_loader():
    fifths_or_tenths = Misc.FIFTHS
    # fifths_or_tenths = Misc.TENTHS

    path = 'results/ga/ga_dipm_fifths/'
    filename = 'ga_dipm_gen_2432_fit_27.txt'

    # path = 'results/ga/ga_scpm_fifths/'
    # filename = 'ga_scpm_gen_0146_fit_19.txt'

    # path = 'results/ga/ga_scpm_tenths/'
    # filename = 'ga_scpm_gen_4066_fit_118.txt'

    model, threshold, fitness_value, data, individual = Loader.load_individual(path + filename)

    export_file = ''
    title = 'GA-' + model.upper() + ', fitness: ' + str(fitness_value)
    exp2(model, individual, data, threshold, fifths_or_tenths, export_file, title)


def main():
    # coordinate_fifths = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
    # coordinates_fifths = [coordinate_fifths, coordinate_fifths]
    # Display.save_simple_abilities_matrix(GoalMatrix.matrix_fifth(), 'GA fifths Goal Matrix', '', coordinates_fifths)

    # coordinate_tenths = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    # coordinates_tenths = [coordinate_tenths, coordinate_tenths]
    # Display.save_simple_abilities_matrix(GoalMatrix.matrix_tenth(), 'GA tenths Goal Matrix', '', coordinates_tenths)

    # print('Fitness value of GA-DIPM: ' + str(Tools.value_for_fitness(Ga_mat.dipm(), GoalMatrix.matrix_tenth())))
    # print('Fitness value of GA-SCPM: ' + str(Tools.value_for_fitness(Ga_mat.scpm(), GoalMatrix.matrix_tenth())))

    # main_exp2()
    main_exp2_loader()

    pass


main()
