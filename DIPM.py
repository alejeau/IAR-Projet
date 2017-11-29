#!/usr/bin/python3
# -*-coding: utf-8 -*

import Tools as Tools


class DIPM():
    def __init__(self):
        # weights
        self.wcs1 = 1.0
        self.wcs2 = 1.0
        self.wsd2_gpe = 1.0
        self.wgpe_stn = 1.0
        self.wsd1_gpi = 1.0
        self.stn_gpi = 1.0

        # threshold
        self.theta_d1 = 0.2
        self.theta_d2 = 0.2
        self.theta_gpe = -0.2
        self.theta_stn = -0.25
        self.theta_gpi = -0.2

        # slope parameter
        self.m = 1.0
        # activation rate
        self.k = 25.0
        # time increment
        self.dt = 1.0

    # StratiumD1
    def u_i_d1(self, y_i_c: float):
        return self.wcs1 * y_i_c

    def y_i_d1(self, a_i_d1: float):
        return self.m * (a_i_d1 - self.theta_d1) * Tools.heaviside_step_function(a_i_d1 - self.theta_d1)

    # StratiumD2
    def u_i_d2(self, y_i_c: float):
        return self.wcs2 * y_i_c

    def y_i_d2(self, a_i_d2: float):
        return self.m * (a_i_d2 - self.theta_d2) * Tools.heaviside_step_function(a_i_d2 - self.theta_d2)

    # GPe
    def u_i_gpe(self, y_i_c: float):
        return (-self.wsd2_gpe) * y_i_c

    def y_i_gpe(self, a_i_gpe: float):
        return self.m * (a_i_gpe - self.theta_gpe) * Tools.heaviside_step_function(a_i_gpe - self.theta_gpe)

    # STN
    def u_i_stn(self, y_i_c: float):
        return (-self.wgpe_stn) * y_i_c

    def y_i_stn(self, a_i_stn: float):
        return self.m * (a_i_stn - self.theta_stn) * Tools.heaviside_step_function(a_i_stn - self.theta_stn)

    # GPi
    def u_i_gpi(self, y_i_c: float):
        return (-self.wsd1_gpi) * y_i_c

    def y_i_gpi(self, a_i_gpi: float):
        return self.m * (a_i_gpi - self.theta_gpi) * Tools.heaviside_step_function(a_i_gpi - self.theta_gpi)

    def delta_a(self, a: float, u: float):
        return a - self.k * (a - u) * self.dt
