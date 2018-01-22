#!/usr/bin/python3
# -*-coding: utf-8 -*

from tools.Abilities import Abilities
from models.matrix.Matrix import Matrix


class GoalMatrix:
    @staticmethod
    def matrix_tenth() -> Matrix:
        mat = [  # in x we store the y
            [Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION],
            [Abilities.NO_SELECTION, Abilities.NO_SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION],
            [Abilities.SELECTION, Abilities.SELECTION, Abilities.NO_SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING],
            [Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.NO_SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING],
            [Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.NO_SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING],
            [Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.NO_SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING],
            [Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.NO_SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING],
            [Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.NO_SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING],
            [Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.NO_SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING],
            [Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.NO_SWITCHING, Abilities.SWITCHING],
            [Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.NO_SWITCHING]
        ]
        matrix = Matrix()
        matrix.init_matrix(mat)
        return matrix

    @staticmethod
    def pprint_tenth():
        GoalMatrix.matrix_tenth().pprint()

    @staticmethod
    def matrix_fifth() -> Matrix:
        mat = [  # in x we store the y
            [Abilities.NO_SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION],
            [Abilities.SELECTION, Abilities.NO_SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING],
            [Abilities.SELECTION, Abilities.SELECTION, Abilities.NO_SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING],
            [Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.NO_SWITCHING, Abilities.SWITCHING, Abilities.SWITCHING],
            [Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.NO_SWITCHING, Abilities.SWITCHING],
            [Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.SELECTION, Abilities.NO_SWITCHING]
        ]
        matrix = Matrix()
        matrix.init_matrix(mat)
        return matrix

    @staticmethod
    def pprint_fifth():
        GoalMatrix.matrix_fifth().pprint()
