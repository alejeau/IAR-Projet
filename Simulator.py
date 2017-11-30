#!/usr/bin/python3
# -*-coding: utf-8 -*

import models.DIPM as DIPM
import models.SCPM as SCPM

class Simulator:
    def __init__(self):
        # default model type is DIPM
        self.model_type = 'dipm'
        self.model = DIPM.DIPM()

    def set_model(self, m_type: str):
        self.model_type = m_type
        self.init_model()

    def init_model(self):
        if self.model_type == 'scpm':
            self.model = SCPM.SCPM()
        else:
            self.model = DIPM.DIPM()

