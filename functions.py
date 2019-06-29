# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 16:36:44 2019

@author: sumukhvaidya
"""
import numpy as np
import cmath

#Defining the particular solution for the transport equation.
#This takes the inverse of the system of equations and returns the coefficients A_i of the particulart solution.
def particularsoln(sigmas, sigmat,r, E0, g):
    X=[[sigmas-sigmat,-sigmat,0,0],[-sigmat,3*(sigmat-g*sigmas),-2*sigmat,0],[0,-2*sigmat,5*(sigmat-g**2*sigmas), -3*sigmat],[0,0,-3*sigmat,7*(sigmat-g**3*sigmas)]]
    p=(E0*sigmas*np.exp(-sigmat*r))/(16*np.pi**2*r**2)
    Y=[[p],[p*g],[p*g**2],[p*g**3]]
    return np.dot(np.linalg.inv(X),Y)

#Define the homogeneous solution of the transport equation.
#This will be used to calculate all 16 coefficients of the soluiton of the homogeneous equation.
def homogeneoussoln(C, sigmat, sigmas,g,):
    #Calculations for the sigma coefficient calculation
    G0=(sigmat-sigmas)
    G1=3*(sigmat-g*sigmas)
    G2=5*(sigmat-g**2*sigmas)
    G3=7*(sigmat-g**3*sigmas)
    mu1= cmath.sqrt((9*G0*G1+4*G0*G3+G2*G3+cmath.sqrt((9*G0*G1+4*G0*G3+G2*G3)**2-36*G0*G1*G2*G3))/18)
    mu2= cmath.sqrt((9*G0*G1+4*G0*G3+G2*G3-cmath.sqrt((9*G0*G1+4*G0*G3+G2*G3)**2-36*G0*G1*G2*G3))/18)
    sigma=min(abs(mu1),abs(mu2))
    #Putting the B together for coefficient calculation
    B=np.zeros(5)
    B[0]=C
    B[1]=C*(sigmat-sigmas)/sigma
    B[2]=C*(-0.5+3*(sigmat-sigmas)*(sigmat-g*sigmas)/sigma**2)
    B[3]=C*(-2*(sigmat-sigmas)/(3*sigma)-(5*(sigmat-g**2*sigmas)*(sigmat-g*sigmas)*(sigmat-sigmas))/(2*sigma**3))
    B[4]=sigma
    return B