#!/usr/bin/python3
# -*-coding: utf-8 -*

from enum import Enum, auto


class AutoName(Enum):
    def _generate_next_value_(self, start, count, last_values):
        return self


class Abilities(AutoName):
    DEFAULT = auto()
    NO_SELECTION = '+'
    SELECTION = '•'
    NO_SWITCHING = '◙'
    SWITCHING = '○'

