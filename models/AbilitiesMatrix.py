#!/usr/bin/python3
# -*-coding: utf-8 -*

from tools.Abilities import Abilities
import pprint


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
        self.matrix = [[]]
        self.threshold = 0.05

    def generate_matrix(self, channel1: {float: float}, channel2: {float: float}, threshold: float):
        self.threshold = threshold
        self.x_keys = sorted(channel1.keys())
        print('self.x_keys: ' + str(self.x_keys))
        self.x_len = len(self.x_keys)
        self.y_keys = sorted(channel2.keys())
        print('self.y_keys: ' + str(self.y_keys))
        self.y_len = len(self.y_keys)

        self.matrix = [[Abilities.DEFAULT] * self.y_len for i in range(self.x_len)]

        i = 0
        for k in self.x_keys:
            self.x_keys_map.update({k: i})
            self.reversed_x_keys_map.update({i: k})
            i += 1

        i = 0
        for k in self.y_keys:
            self.y_keys_map.update({k: i})
            self.reversed_y_keys_map.update({i: k})
            i += 1

        for x in self.x_keys:
            i = self.x_keys_map[x]
            for y in self.y_keys:
                j = self.y_keys_map[x]
                value = Abilities.SELECTION
                if channel1[x] >= threshold and channel2[y] >= threshold:
                    value = Abilities.NO_SELECTION
                elif channel1[x] < threshold and channel2[y] < threshold:
                    value = Abilities.NO_SWITCHING
                # There might be some switching from chan2 to chan1 but it's not explicitly detailed in the paper,
                # so I have not included that.
                elif channel2[y] < threshold <= channel1[x]:
                    prev_x = self.reversed_x_keys_map[i-1]
                    if channel1[prev_x] < threshold:
                        value = Abilities.SWITCHING

                self.matrix[i][j] = value

    def get_x_keys(self):
        return self.x_keys

    def get_y_keys(self):
        return self.y_keys

    def get(self, x: float, y: float):
        return self.matrix[self.x_keys_map[x]][self.y_keys_map[y]]

    def normal_print(self):
        print(self.matrix)

    def pretty_print(self):
        pp = pprint.PrettyPrinter(indent=0)
        pp.pprint(self.matrix)
