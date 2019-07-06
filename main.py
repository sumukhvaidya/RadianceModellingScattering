import numpy as np
import scipy
import cmath
import functions
import radiance
import approx_reflectance


#To C, give a 4 element vector, all else is scalars.
sigmat=2300
sigmas=1800
E0=1e-2
g=0.1
r=0.01
mu=0.2
C=[.01,.01,.01,.01]
L=radiance.radiance(sigmat,sigmas,E0,g,r,mu,C)
