#!/usr/bin/python3
# -*-coding: utf-8 -*

from tools.Abilities import Abilities
from models.matrix.Matrix import Matrix


def heaviside_step_function(number):
    return 0 if number < 0 else 1


def normalized_number(size: int, number: int) -> str:
    n = str(number)
    tmp = ''
    s = size - len(n)
    for i in range(0, s):
        tmp += '0'

    return tmp + n


def get_numerical_value_of_ability(ability: Abilities) -> int:
    if ability is Abilities.NO_SELECTION:
        return 0
    if ability is Abilities.SELECTION:
        return 1
    if ability is Abilities.NO_SWITCHING:
        return 2
    if ability is Abilities.SWITCHING:
        return 3


def generate_simple_ability_matrix(channel1: {float: float}, channel2: {float: float}, threshold: float):
    x_keys_map = {}
    reversed_x_keys_map = {}
    y_keys_map = {}
    reversed_y_keys_map = {}
    matrix = Matrix()
    x_keys = sorted(channel1.keys())
    x_len = len(x_keys)
    y_keys = sorted(channel2.keys())
    y_len = len(y_keys)

    tmp_matrix = [[Abilities.NO_SELECTION] * y_len for _ in range(x_len)]

    i = 0
    for k in x_keys:
        x_keys_map.update({k: i})
        reversed_x_keys_map.update({i: k})
        i += 1

    i = 0
    for k in y_keys:
        y_keys_map.update({k: i})
        reversed_y_keys_map.update({i: k})
        i += 1

    for x in x_keys:
        i = x_keys_map[x]
        for y in y_keys:
            j = y_keys_map[y]
            if channel1[x] <= threshold or channel2[y] <= threshold:
                value = Abilities.SELECTION
                if channel2[y] <= threshold < channel1[x]:
                    if i != 0:
                        prev_x = reversed_x_keys_map[i-1]
                        if channel2[prev_x] <= threshold:
                            value = Abilities.SWITCHING
                elif channel1[x] <= threshold and channel2[y] <= threshold and i != 0 and j != 0:
                    value = Abilities.NO_SWITCHING

                tmp_matrix[i][j] = value
    matrix.init_matrix(tmp_matrix)
    return matrix


def get_reward(evaluated: Abilities, goal: Abilities) -> int:
    num_evaluated = get_numerical_value_of_ability(evaluated)
    num_goal = get_numerical_value_of_ability(goal)
    res = num_evaluated - num_goal
    if evaluated is Abilities.NO_SWITCHING:  # NO_SWITCHING is BAD
        res -= 1
    return res


def value_for_fitness(test: Matrix, goal: Matrix) -> float:
    x_len = test.get_x_len()
    y_len = test.get_y_len()

    fitness_value = 0
    for x in range(x_len):
        for y in range(y_len):
            fitness_value += get_reward(test.get_item(x, y), goal.get_item(x, y))

    return fitness_value


def update_conf(conf: {}, param: [str], value: [float]) -> {}:
    for i in range(len(param)):
        conf.update({param[i]: value[i]})
    return conf
