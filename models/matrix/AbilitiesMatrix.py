#!/usr/bin/python3
# -*-coding: utf-8 -*

from tools.Abilities import Abilities
from models.matrix.Matrix import Matrix


class AbilitiesMatrix:
    def __init__(self):
        self.x_keys = []
        self.y_keys = []
        self.x_len = 0
        self.y_len = 0
        self.x_keys_map = {}
        self.reversed_x_keys_map = {}
        self.y_keys_map = {}
        self.reversed_y_keys_map = {}
        self.matrix = Matrix()
        self.threshold = 0.05


    def get_x_keys(self):
        return self.x_keys

    def get_y_keys(self):
        return self.y_keys

    def get_value(self, x_key: float, y_key: float):
        return self.matrix.get_item(self.x_keys_map[x_key], self.y_keys_map[y_key])

    def pretty_print(self):
        self.matrix.pprint()

    def get_matrix(self) -> Matrix:
        return self.matrix
