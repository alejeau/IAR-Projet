#!/usr/bin/python3
# -*-coding: utf-8 -*

from tools.Abilities import Abilities

def heaviside_step_function(number):
    return 0 if number < 0 else 1


def get_numerical_value_of_ability(ability: Abilities.value) -> int:
    if ability is Abilities.NO_SELECTION:
        return 0
    if ability is Abilities.SELECTION:
        return 1
    if ability is Abilities.NO_SWITCHING:
        return 2
    if ability is Abilities.SWITCHING:
        return 3
