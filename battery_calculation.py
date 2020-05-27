# -*- coding: utf-8 -*-
"""
Created on Wed May 27 19:33:57 2020

@author: Akaash Preetham
"""

import math
from calculation import Calculation
'''
car = Calculation(10000, 6.282, 0.05, 0.8, 0.01, 0.4, 10, 100, 0)
car.speed
bus = Calculation()
bus.speed
'''

rho = 1.225
Cd = 0.8
A = 6.282
M = 10000
Crr = 0.01
g = 9.81

class Battery:
    
    energy = 0
    
    
    def __init__(self):
        self.energy = 0
        self.ti = 0
        self.tf = 0
        self.vi = 0
        self.vf = 0
        self.distance = 0
    
    def idle(self, time):
        time = time * 60
        self.ti = self.ti + time
        self.tf = self.ti
        
    def accelerate(self, vfrom, vto, acceleration):
        vfrom = vfrom * 5/18
        vto = vto * 5/18
        self.vi = vfrom
        self.vf = vto
        t = (self.vf - self.vi)/acceleration
        self.ti = self.tf
        self.tf = self.ti + t
        self.distance = float(self.distance + ((pow(self.vf, 2) - pow(self.vi, 2))/(2*acceleration))/1000)
        self.energy = self.energy + ((0.125 * rho * Cd * A * (pow(self.vf, 4) - pow(self.vi, 4)) + 0.5 * (M * g * Crr + M * acceleration) * (pow(self.vf, 2) - pow(self.vi, 2)))/acceleration)/(1000*3600)
        return self.energy
    
    def cruise(self, vcruise, time):
        vcruise = vcruise * 5/18
        time = time * 60
        self.vi = vcruise
        self.vf = vcruise
        self.ti = self.tf
        self.tf = self.ti + time
        self.distance = float(self.distance + (vcruise * time)/(1000))
        self.energy = self.energy + ((0.5 * rho * Cd * A * pow(vcruise, 3) + M * g * Crr * vcruise) * time)/(1000 * 3600)
        return self.energy
    
    def decelerate(self, vfrom, vto, acceleration):
        vfrom = vfrom * 5/18
        vto = vto * 5/18
        self.distance = self.distance + (-pow(vto, 2) + pow(vfrom, 2)/(2 * acceleration))/1000
        self.energy = self.energy - ((M * pow(vfrom, 2) - M * pow(vto, 2))/3600000)
        return self.energy
        
    def energy_required(self, v_range):
        return self.energy/self.distance * v_energy * 1.5

Li = Battery()
Li.idle(2)
Li.accelerate(0, 25, 0.115)
Li.accelerate(25, 45, 0.03)
Li.cruise(45, 3)
Li.decelerate(45, 25, 0.023)
Li.cruise(25, 10)
Li.decelerate(25, 15, 0.041)
Li.cruise(15, 3)
Li.decelerate(15, 0, 0.023)
Li.energy
Li.distance

v_range = float(input('Enter driving range '))
energy_battery = Li.energy/Li.distance * v_range * 1.5
print(energy_battery)
