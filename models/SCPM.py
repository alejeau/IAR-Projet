#!/usr/bin/python3
# -*-coding: utf-8 -*

from tools import Tools as Tools


class SCPM:
    def __init__(self):

        # activation
        self.a_d1 = 0.2
        self.a_d2 = 0.2
        self.a_gpe = 0.2
        self.a_stn = 0.2
        self.a_gpi = 0.2

        # weights
        self.wcs1 = 1.0
        self.wcs2 = 1.0
        self.wsd2_gpe = 1.0
        self.wstn_gpe = 1.0
        self.wc_stn = 1.0
        self.wgpe_stn = 1.0
        self.wsd1_gpi = 1.0
        self.stn_gpi = 1.0
        self.wgpe_gpi = 1.0

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

        # storage of y_d1
        self.y_d1 = 0.0

    # StratiumD1
    def u_d1(self, y_c: float):
        return self.wcs1 * y_c

    def y_d1(self, a_d1: float):
        return self.m * (a_d1 - self.theta_d1) * Tools.heaviside_step_function(a_d1 - self.theta_d1)

    # StratiumD2
    def u_d2(self, y_c: float):
        return self.wcs2 * y_c

    def y_d2(self, a_d2: float):
        return self.m * (a_d2 - self.theta_d2) * Tools.heaviside_step_function(a_d2 - self.theta_d2)

    # GPe
    def u_gpe(self, y_d2: float, y_stn: list):
        return (-self.wsd2_gpe) * y_d2 + self.wstn_gpe * sum(y_stn)

    def y_gpe(self, a_gpe: float):
        return self.m * (a_gpe - self.theta_gpe) * Tools.heaviside_step_function(a_gpe - self.theta_gpe)

    # STN
    def u_stn(self, y_c: float, y_gpe: float):
        return (-self.wc_stn) * y_c - self.wgpe_stn * y_gpe

    def y_stn(self, a_stn: float):
        return self.m * (a_stn - self.theta_stn) * Tools.heaviside_step_function(a_stn - self.theta_stn)

    # GPi
    def u_gpi(self, y_sd1: float, y_stn: list, y_gpe: float):
        return (-self.wsd1_gpi) * y_sd1 + self.wstn_gpe * sum(y_stn) - self.wgpe_gpi * y_gpe

    def y_gpi(self, a_gpi: float):
        return self.m * (a_gpi - self.theta_gpi) * Tools.heaviside_step_function(a_gpi - self.theta_gpi)

    def delta_a(self, a: float, u: float) -> float:
        return a - self.k * (a - u) * self.dt

    def compute_stn(self, salience) -> float:
        # we have the salience, we now need a_xxx
        # we also probably need to store the past values

        # d1
        u_d1 = self.u_d1(salience)
        self.a_d1 = self.delta_a(self.a_d1, u_d1)
        # print('delta_d1: ' + str(self.a_d1))
        self.y_d1 = self.y_d1(self.a_d1)

        # d2
        u_d2 = self.u_d2(salience)
        self.a_d2 = self.delta_a(self.a_d2, u_d2)
        # print('delta_d2: ' + str(self.a_d2))
        y_d2 = self.y_d2(self.a_d2)

        # # stn
        # u_stn = self.u_stn(y_gpe)
        # self.a_stn = self.delta_a(self.a_stn, u_stn)
        # # print('delta_stn: ' + str(self.a_stn))
        # y_stn = self.y_stn(self.a_stn)

        return y_stn