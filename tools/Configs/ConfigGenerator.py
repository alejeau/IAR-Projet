#!/usr/bin/python3
# -*-coding: utf-8 -*

import tools.Archivist as Archivist
import tools.Configs.Models as Models
import tools.Configs.ConfigExp1 as ConfigExp1
import tools.Configs.ConfigExp2 as ConfigExp2


class ConfigGenerator:
    @staticmethod
    def generate_models():
        Archivist.store(Models.get_dipm_base_generator(), '../../configs/dipm_base.p')
        Archivist.store(Models.get_scpm_base_generator(), '../../configs/scpm_base.p')

    @staticmethod
    def generate_config_exp1():
        Archivist.store(ConfigExp1.config_dipm_exp1(), '../../configs/config_dipm_exp1.p')
        Archivist.store(ConfigExp1.config_scpm_exp1(), '../../configs/config_scpm_exp1.p')

    @staticmethod
    def generate_config_exp2():
        Archivist.store(ConfigExp2.config_dipm_exp2(), '../../configs/config_dipm_exp2.p')
        Archivist.store(ConfigExp2.config_scpm_exp2(), '../../configs/config_scpm_exp2.p')

    @staticmethod
    def generate_all():
        ConfigGenerator.generate_models()
        ConfigGenerator.generate_config_exp1()
        ConfigGenerator.generate_config_exp2()


ConfigGenerator.generate_all()
