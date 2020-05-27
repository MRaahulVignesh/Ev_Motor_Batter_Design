# -*- coding: utf-8 -*-
"""
Created on Mon May 25 12:42:58 2020

@author: Akaash Preetham
"""

"""
Libraries
"""
import math


"""
Standard specifications and physical constants of vehicle
"""

g = 9.81
rho = 1.225

class Calculation:
    
    motor_poles = 12
    motor_v_rated = 400
    speed_at_maxtorque = 1000
    a_time = 10
    
    def __init__(self, v_weight = 0, v_area = 0, slip = 0, Cd = 0, Crr = 0, wheel_radius = 0, gear_ratio = 0, v_speed = 0, grade = 0):
        self.weight = v_weight
        self.area = v_area
        self.slip = slip
        self.Cd = Cd
        self.Crr = Crr
        self.wheel_radius = wheel_radius
        self.gear_ratio = gear_ratio
        self.speed = v_speed * 5/18
        self.grade = math.atan(grade/100)
        
    def speedChange(self, v_speed):
        self.speed = v_speed * 5/18
        
    def gradeChange(self, grade):
        self.grade = math.atan(grade/100)
        
    def accelerate(self):
        acceleration = self.speed/self.a_time
        return acceleration
        
    def force(self, v_wind):
        F_t = (self.weight * self.accelerate() + self.weight * g * self.Crr * math.cos(self.grade) + 0.5 * rho * self.area * self.Cd * pow(self.speed-v_wind, 2) + self.weight * g * math.sin(self.grade))
        return F_t
        
    def power(self, v_wind):
        return self.force(v_wind) * self.speed

    def motor(self, v_wind):
        wheel_speed = math.ceil((self.speed * 60)/(2 * math.pi * self.wheel_radius))
        wheel_torque = self.force(v_wind) * self.wheel_radius
        motor_torque = wheel_torque/self.gear_ratio
        return motor_torque

    





