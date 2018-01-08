#!/usr/bin/python3
# -*-coding: utf-8 -*

from tools.Abilities import Abilities
from tools import Display


class BaseMatrices:
    @staticmethod
    def dipm():
        matrix = [
            [Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION],
            [Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION],
            [Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION],
            [Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION],
            [Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION],
            [Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION],
            [Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION],
            [Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.NO_SWITCHING, Abilities.NO_SWITCHING, Abilities.NO_SWITCHING, Abilities.NO_SWITCHING],
            [Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.NO_SWITCHING, Abilities.NO_SWITCHING, Abilities.NO_SWITCHING, Abilities.NO_SWITCHING],
            [Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.NO_SWITCHING, Abilities.NO_SWITCHING, Abilities.NO_SWITCHING, Abilities.NO_SWITCHING],
            [Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.NO_SWITCHING, Abilities.NO_SWITCHING, Abilities.NO_SWITCHING, Abilities.NO_SWITCHING]
        ]
        return matrix

    @staticmethod
    def scpm():
        matrix = [
            [Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION],
            [Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION],
            [Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION],
            [Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION],
            [Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.NO_SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION],
            [Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SWITCHING, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION],
            [Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION],
            [Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION],
            [Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.NO_SWITCHING, Abilities.NO_SWITCHING, Abilities.SELECTION],
            [Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.NO_SWITCHING, Abilities.NO_SWITCHING, Abilities.NO_SWITCHING],
            [Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.NO_SWITCHING, Abilities.NO_SWITCHING]
        ]
        return matrix
