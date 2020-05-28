import math

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
        return self.energy/self.distance * v_range * 1.5

