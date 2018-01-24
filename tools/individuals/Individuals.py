#!/usr/bin/python3
# -*-coding: utf-8 -*

from enum import Enum
from tools.individuals.loader import Loader


class GaDipmFifths(Enum):
    FIT_29_GEN5_401 = [0.7965933524729384, 0.9933189996262195, 0.7498378125116993, 0.7562354658044542,
                       0.7841440060395849, 0.765171786187149, 0.2022375727033796, 0.32917845471779494,
                       -0.5328443795460719, -0.4129138058219399, -0.1467758116462642]


class GaScpmFifths(Enum):
    FIT_36_GEN_211 = [0.9436127620587037, 0.8584516982693315, 0.1110883501279798, 0.9531355801266248,
                      0.6703181414826133, 0.9835373422344036, 0.47220458868287896, 0.9112781093201476,
                      0.19463876000364744, 0.09694758287977512, 0.19840543456412973, -0.5522206219458731,
                      -0.2467925406284387, -0.19850047159492523]
    FIT_36_GEN_442 = [0.8221177991284111, 0.8584516982693315, 0.1110883501279798, 0.9531355801266248,
                      0.8580049847868573, 0.9947307598125508, 0.35007412368840685, 0.9112781093201476,
                      0.19463876000364744, 0.09694758287977512, 0.19840543456412973, -0.5522206219458731,
                      -0.2467925406284387, -0.19850047159492523]


class GaScpmTenths(Enum):
    FIT_121_GEN_4290 = [0.902498432648584, 0.6209853301100781, 0.9669396134356035, 0.8846160771831636,
                        0.56777419541111, 0.5856100311684512, 0.601248348375428, 0.7360289437228867,
                        0.23646095040712833, 0.02422933111564063, 0.8204958083999463, -0.22822586090189623,
                        -0.009401080785316429, -0.17511521446431288]
    FIT_121_GEN_4891 = [0.9163850320862632, 0.6209853301100781, 0.9669396134356035, 0.8846160771831636,
                        0.56777419541111, 0.5918221323637465, 0.22384188519786963, 0.5152216731728826,
                        0.23646095040712833, 0.02422933111564063, 0.8204958083999463, -0.22822586090189623,
                        -0.009401080785316429, -0.17511521446431288]
