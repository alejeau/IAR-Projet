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
        self.dt = 0.001

        # storage of y_xxx values
        self.y_d1 = 0.0
        self.y_d2 = 0.0
        self.y_gpe = 0.0
        self.y_stn = 0.0
        self.y_gpi = 0.0

    def get_theta_gpi(self) -> float:
        return self.theta_gpi
        
    def get_dt(self) -> float:
        return self.dt

    # StratiumD1
    def u_i_d1(self, y_c: float):
        return self.wcs1 * y_c

    def y_i_d1(self, a_d1: float):
        return self.m * (a_d1 - self.theta_d1) * Tools.heaviside_step_function(a_d1 - self.theta_d1)

    # StratiumD2
    def u_i_d2(self, y_c: float):
        return self.wcs2 * y_c

    def y_i_d2(self, a_d2: float):
        return self.m * (a_d2 - self.theta_d2) * Tools.heaviside_step_function(a_d2 - self.theta_d2)

    # GPe
    def u_i_gpe(self, y_d2: float, y_stn: list):
        return (-self.wsd2_gpe) * y_d2 + self.wstn_gpe * sum(y_stn)

    def y_i_gpe(self, a_gpe: float):
        return self.m * (a_gpe - self.theta_gpe) * Tools.heaviside_step_function(a_gpe - self.theta_gpe)

    # STN
    def u_i_stn(self, y_c: float, y_gpe: float):
        return (-self.wc_stn) * y_c - self.wgpe_stn * y_gpe

    def y_i_stn(self, a_stn: float):
        return self.m * (a_stn - self.theta_stn) * Tools.heaviside_step_function(a_stn - self.theta_stn)

    # GPi
    def u_i_gpi(self, y_d1: float, y_stn: list, y_gpe: float):
        return (-self.wsd1_gpi) * y_d1 + self.wstn_gpe * sum(y_stn) - self.wgpe_gpi * y_gpe

    def y_i_gpi(self, a_gpi: float):
        return self.m * (a_gpi - self.theta_gpi) * Tools.heaviside_step_function(a_gpi - self.theta_gpi)

    def delta_a(self, a: float, u: float) -> float:
        return a - self.k * (a - u) * self.dt

    def compute_d1(self, salience: float) -> float:
        u_d1 = self.u_i_d1(salience)
        self.a_d1 = self.delta_a(self.a_d1, u_d1)
        self.y_d1 = self.y_i_d1(self.a_d1)
        return self.y_d1
        
    def compute_d2(self, salience: float) -> float:
        u_d2 = self.u_i_d2(salience)
        self.a_d2 = self.delta_a(self.a_d2, u_d2)
        self.y_d2 = self.y_i_d2(self.a_d2)
        return self.y_d2
    
    # requires previous values of stn outputs (at t-1)
    def compute_gpe(self, y_d2: float, prev_stn_list: [float]) -> float:
        u_gpe = self.u_i_gpe(y_d2, prev_stn_list)
        self.a_gpe = self.delta_a(self.a_gpe, u_gpe)
        self.y_gpe = self.y_i_gpe(self.a_gpe)
        return self.y_gpe

    def compute_stn(self, salience: float, y_gpe: float) -> float:
        u_stn = self.u_i_stn(salience, y_gpe)
        self.a_stn = self.delta_a(self.a_stn, u_stn)
        self.y_stn = self.y_i_stn(self.a_stn)
        return self.y_stn

    # assumes y_d1 has been computed
    def compute_gpi(self, stn_list: [float]) -> float:
        u_gpi = self.u_i_gpi(self.y_d1, stn_list, self.y_gpe)
        self.a_gpi = self.delta_a(self.a_gpi, u_gpi)
        self.y_gpi = self.y_i_gpi(self.a_gpi)
        return self.y_gpi

    def compute_d1_to_stn(self, salience: float, prev_stn_list: [float]) -> {str: float}:
        y_d1 = self.compute_d1(salience)
        y_d2 = self.compute_d2(salience)
        y_gpe = self.compute_gpe(y_d2, prev_stn_list)
        y_stn = self.compute_stn(salience, y_gpe)

        return {'y_d1': y_d1, 'y_d2': y_d2, 'y_gpe': y_gpe, 'y_stn': y_stn}
        
    def compute_d1_to_gpi(self, salience: float, prev_stn_list: [float], current_stn_list: [float]) -> {str: float}:
        vals = self.compute_d1_to_stn(salience, prev_stn_list)
        y_gpi = self.compute_gpi(current_stn_list)
        vals.update('y_gpi': y_gpi)
        return vals
        
    def load_conf(self, filename: str):
        conf = confLoader.load(filename)
        self.a_d1 = conf['a_d1']
        self.a_d2 = conf['a_d2']
        self.a_gpe = conf['a_gpe']
        self.a_stn = conf['a_stn']
        self.a_gpi = conf['a_gpi']
        self.wcs1 = conf['wcs1']
        self.wcs2 = conf['wcs2']
        self.wsd2_gpe = conf['wsd2_gpe']
        self.wgpe_stn = conf['wgpe_stn']
        self.wsd1_gpi = conf['wsd1_gpi']
        self.stn_gpi = conf['stn_gpi']
        self.theta_d1 = conf['theta_d1']
        self.theta_d2 = conf['theta_d2']
        self.theta_gpe = conf['theta_gpe']
        self.theta_stn = conf['theta_stn']
        self.theta_gpi = conf['theta_gpi']
        self.m = conf['m']
        self.k = conf['k']
        self.dt = conf['dt']
        self.y_d1 = conf['y_d1']
        self.y_d2 = conf['y_d2']
        self.y_gpe = conf['y_gpe']
        self.y_stn = conf['y_stn']
        self.y_gpi = conf['y_gpi']
