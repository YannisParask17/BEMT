# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 23:41:01 2023

@author: Ioannis Prsk
"""
import numpy as np

class Rotor:
    
    def __init__(self, N_blades, R):
        self.N_blades = N_blades
        self.R = R

    
    def discretise_blade(self, N_radial, blade_start=.2, method="linear"):
        self.N_radial = N_radial
        
        if method == "linear":
            self.r_ends = np.linspace(blade_start, self.R, self.N_radial+1) # linear discretisation
        
        else:
            
            self.r_ends = blade_start + (np.sin(np.linspace(-np.pi/2, np.pi/2,  self.N_radial+1))/2+0.5)*(self.R-blade_start) # sinusoidal discretisation
                
        self.r_centre = (self.r_ends[1:] + self.r_ends[:-1])/2 # radial location of the centre of annuli
        self.mu = self.r_centre/self.R # non dimensional radial location of the centre of annuli
        
        
    def set_operation(self, Uinf, tsr):
        self.Uinf   = Uinf # free stream velocity [m/s]
        self.tsr    = tsr  # tip speed ratio
        self.omega  = Uinf * tsr / self.R # rotor speed [rad/s]
        

    def set_rotor(self, discr_params, oper_condition):
        """
        discretise the blade and set the operational parameters

        Returns
        -------
        None.

        """
        
        
        pass
    


# set_blade -> discretise blade and set operational parameters

rotor_test = Rotor(3, 100)
rotor_test.discretise_blade(100,.2,"sin")
rotor_test.set_operation(10, 8)