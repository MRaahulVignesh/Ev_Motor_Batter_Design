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

v_weight = float(input('Enter vehicle weight '))
v_width = float(input('Enter vehicle width '))
v_height = float(input('Enter vehicle height '))
v_area = float(input('Enter vehicle frontal area '))
slip = float(input('Enter vehicle slip ratio '))
Cd = float(input('Enter drag coefficient '))
Crr = float(input('Enter coefficient of rolling resistance '))

g = 9.81
rho = 1.225

"""
Gradability specifications
"""

grade_percent = float(input('Enter gradability percent '))
grade = (math.atan(grade_percent/100))
v_speed = float(input('Enter grade speed in km/hr '))*5/18
#time taken to accelerate
a_time = 10                                             
acceleration = v_speed/a_time
v_wind = float(input('Enter wind speed '))

"""
Power
"""

F_t = (v_weight * acceleration + v_weight * g * Crr * math.cos(grade) + 0.5 * rho * v_area * Cd * pow(v_speed-v_wind,2) + v_weight * g * math.sin(grade))
P_t = F_t * v_speed

"""
Motor specifications

Type: PMSM
Number of stator phases: 3, 6 or 9
Operating speed: 0-3400 rpm
"""

m_v_rated = 400
m_poles = 12

wheel_radius = float(input('Enter wheel radius '))
wheel_speed = math.ceil((v_speed * 60)/(2 * math.pi * wheel_radius))
wheel_torque = F_t * wheel_radius

gear_ratio = float(input('Enter gear ratio '))
speed_at_maxtorque = 1000

motor_torque = wheel_torque/gear_ratio


"""
Battery specifications
"""

total_capacity = 24

energy_demanded_observation = 0.528
distance_travelled_observation = 0.793
energy_per_distance = energy_demanded_observation / distance_travelled_observation

distance_travelled = float(input('Enter distance travelled '))
energy_required = energy_per_distance * distance_travelled * 1.5 #considering auxillary battery

no_of_modules = math.floor(energy_required / total_capacity)





