#!/usr/bin/python3
# -*-coding: utf-8 -*

from tools.Abilities import Abilities
from models.matrix.Matrix import Matrix
from tools import Archivist


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


def determine_ability(outputs: {}, dt: float, threshold: float) -> Abilities:
    chan1 = outputs[0]
    keys_chan1 = chan1.keys()
    chan2 = outputs[1]

    pas_par_seconde = (1 / dt)
    selected = 0
    for t in range(int(1 * pas_par_seconde), int(2 * pas_par_seconde + 1)):
        if chan1[t] <= threshold:
            selected += 1
    chan1_i1_selected = True if selected >= 0.8 * pas_par_seconde else False

    chan1_never_selected = True
    for t in keys_chan1:
        if chan1[t] <= threshold:
            chan1_never_selected = False
            break

    selected_chan1 = 0
    selected_chan2 = 0
    for t in range(int(2 * pas_par_seconde + 1), int(len(chan2))):
        if chan1[t] <= threshold:
            selected_chan1 += 1
        if chan2[t] <= threshold:
            selected_chan2 += 1
    chan1_i2_selected = True if selected_chan1 >= 0.8 * (len(chan2) - (2 * pas_par_seconde + 1)) else False
    chan2_selected = True if selected_chan2 >= 0.8 * (len(chan2) - (2 * pas_par_seconde + 1)) else False

    ability = Abilities.NO_SELECTION
    if (chan1_i1_selected and not chan2_selected) or (chan1_never_selected and chan2_selected):
        ability = Abilities.SELECTION
    elif chan1_i1_selected and chan1_i2_selected and chan2_selected:
        ability = Abilities.NO_SWITCHING
    elif chan1_i1_selected and not chan1_i2_selected and chan2_selected:
        ability = Abilities.SWITCHING

    return ability


def get_reward(evaluated: Abilities, goal: Abilities) -> int:
    res = 0
    if evaluated is goal:
        res = 1
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


def store_progress(text: [], model: str, iteration: int):
    filename = 'results/ga_' + model + '_results_' + str(iteration)
    Archivist.store_text(text, filename + '.txt')
