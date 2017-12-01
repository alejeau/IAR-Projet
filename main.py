#!/usr/bin/python3
# -*-coding: utf-8 -*

import Simulator.DIPMSimulator as dipm_sim

sim = dipm_sim.DIPMSimulator()
sim.init_and_load_config('configs/sim1.p')
sim.run_sim('results/results_sim_1.p')
