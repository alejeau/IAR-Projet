#!/usr/bin/python3
# -*-coding: utf-8 -*

import tools.Archivist as Archivist
import tools.Configs.Models as Models
import tools.Configs.ConfigExp1 as ConfigExp1
import tools.Configs.ConfigExp2 as ConfigExp2


class ConfigGenerator:
    @staticmethod
    def generate_models():
        Archivist.store_data(Models.get_dipm_base_generator(), '../../configs/dipm_base.p')
        Archivist.store_data(Models.get_dipm_improved_generator(), '../../configs/dipm_improved.p')
        Archivist.store_data(Models.get_scpm_base_generator(), '../../configs/scpm_base.p')
        Archivist.store_data(Models.get_scpm_improved_generator(), '../../configs/scpm_improved.p')

    @staticmethod
    def generate_config_exp1():
        Archivist.store_data(ConfigExp1.config_dipm_exp1_3_channels(), '../../configs/config_dipm_exp1.p')
        Archivist.store_data(ConfigExp1.config_scpm_exp1_3_channels(), '../../configs/config_scpm_exp1.p')

    @staticmethod
    def generate_config_exp2():
        Archivist.store_data(ConfigExp2.config_dipm_exp2(), '../../configs/config_dipm_exp2.p')
        Archivist.store_data(ConfigExp2.improved_config_dipm_exp2(), '../../configs/config_improved_dipm_exp2.p')
        Archivist.store_data(ConfigExp2.config_scpm_exp2(), '../../configs/config_scpm_exp2.p')
        Archivist.store_data(ConfigExp2.improved_config_scpm_exp2(), '../../configs/config_improved_scpm_exp2.p')

    @staticmethod
    def generate_all():
        ConfigGenerator.generate_models()
        ConfigGenerator.generate_config_exp1()
        ConfigGenerator.generate_config_exp2()


ConfigGenerator.generate_all()
