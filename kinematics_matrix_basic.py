# -*- coding: utf-8 -*-
"""
Created on Sat May 09 11:17:52 2015

@author: Surbhi
"""
import numpy as np
import sympy

#transformation matrix for rotation by th angle about z-axis
def rotate_z(th):
    M = np.mat([[sympy.cos(th), -sympy.sin(th), 0, 0],[sympy.sin(th), sympy.cos(th), 0, 0],[0, 0, 1, 0],[0, 0, 0, 1]])
    return M

# transformation matrix for rotation by th angle about y-axis    
def rotate_y(th):
    M = np.mat([[sympy.cos(th),0,sympy.sin(th),0],[0,1,0,0],[-sympy.sin(th),0,sympy.cos(th),0],[0,0,0,1]])
    return M

# transformation matrix for rotation by th angle about x-axis    
def rotate_x(th):
    M = np.mat([[1,0,0,0],[0,sympy.cos(th),-sympy.sin(th),0],[0,sympy.sin(th),sympy.cos(th),0],[0,0,0,1]])
    return M

# transformation matrix for translation by x units about x-axis
def translate_x(x):
    M = np.mat([[1,0,0,x],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
    return M

#transformation matrix for translation by y units about y-axis    
def translate_y(y):
    M = np.mat([[1,0,0,0],[0,1,0,y],[0,0,1,0],[0,0,0,1]])
    return M

#transformation matrix for translation by z units about z-axis
def translate_z(z):
    M = np.mat([[1,0,0,0],[0,1,0,0],[0,0,1,z],[0,0,0,1]])
    return M
    
# returns the resultant vector after the given vector undergoes global transformations listed in listoftransforms      
def transform_any(listoftranforms, vector):
    for i in listoftranforms:
        vector = i*vector
    return vector
 
#returns transformation matrix for a row of D-H parameters table with parameters: th (rotation about z-axis), d (translation about local z-axis), a (translation about local x-axis), alpha (rotation about local x-axis)   
def transformation_local(th, d, a, alpha):
    M = rotate_z(th)*translate_z(d)*translate_x(a)*rotate_x(alpha)
    return M
