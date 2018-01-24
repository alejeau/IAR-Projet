#!/usr/bin/python3
# -*-coding: utf-8 -*

from tools import Archivist
import copy


class Loader:
    @staticmethod
    def load_individual(filename: str):
        content = Archivist.load_txt(filename)
        model = content[0]
        threshold = float(content[1])
        strip = ['[', ']', '(', ')', '\'']
        data = Loader.strip_and_split(content[2], strip, ', ')
        tmp = Loader.strip_and_split(content[3], strip, ', ')
        fitness_value = int(tmp.pop(0))
        individual = [float(s) for s in tmp]

        return model, threshold, fitness_value, data, individual

    @staticmethod
    def strip_and_split(txt: str, chars: [str], splitter: str) -> [str]:
        tmp = copy.deepcopy(txt)
        for char in chars:
            tmp = tmp.replace(char, '')

        return tmp.split(splitter)
