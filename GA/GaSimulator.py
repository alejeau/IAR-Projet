#!/usr/bin/python3
# -*-coding: utf-8 -*

import Simulator.DIPMSimulator as DipmSim
import Simulator.SCPMSimulator as ScpmSim
from models.matrix.Matrix import Matrix
from tools.Abilities import Abilities
from tools import Tools
from tools.Values import Misc

# inputs for the two channels
fifths = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
tenths = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]


class GaSimulator:

    @staticmethod
    def run_sims(model: str, conf: {}, fifths_or_tenths=Misc.TENTHS) -> {}:
        sim = None
        results = {}

        salience = fifths if fifths_or_tenths is 'fifths' else tenths

        for sc1 in salience:
            sal1 = [0.0] + [sc1 for _ in range(5)]
            for sc2 in salience:
                sal2 = [0.0, 0.0] + [sc2 for _ in range(4)]

                # input pair
                sal = {
                    0: sal1,
                    1: sal2
                }
                conf.update({'salience': sal})

                if model == 'dipm':
                    sim = DipmSim.DIPMSimulator()
                elif model == 'scpm':
                    sim = ScpmSim.SCPMSimulator()

                sim.init_with_config(conf)
                res = sim.run_sim('')
                results.update({(sc1, sc2): res})

        return results

    # generates the matrix of outputs
    @staticmethod
    def analyze_results(results: [{}], conf: {}, threshold, fifths_or_tenths=Misc.TENTHS) -> Matrix:
        dt = conf['dt']
        salience = fifths if fifths_or_tenths == Misc.FIFTHS else tenths

        matrix = Matrix()
        tmp_matrix = [[Abilities.NO_SELECTION] * len(salience) for _ in range(len(salience))]

        i = 0
        for sc1 in salience:
            j = 0
            for sc2 in salience:
                outputs = results[(sc1, sc2)]
                gpi_outputs = outputs['gpi_outputs']
                ability = Tools.determine_ability(gpi_outputs, dt, threshold)
                tmp_matrix[i][j] = ability
                j += 1
            i += 1

        matrix.init_matrix(tmp_matrix)
        return matrix
