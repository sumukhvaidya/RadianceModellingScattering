import numpy as np
import scipy.special
import cmath
import functions


#Take some initial 4 element vector C and find out the radiance based on it. Need to match it to the Fresnel reflection coefficient
# so as to extract the value of C.
def radiance(sigmat,sigmas,E0,g,r,mu,C):
#sigmat=5
#sigmas=5
#E0=1e-4
#g=0.1
#r=0.1
#mu=0

    A= functions.particularsolncoeffs(sigmas, sigmat,r, E0, g)
    
#    C=np.zeros(4)
    B=np.zeros((5,5))
    for i in range(4):
        B[i,:]=functions.homogeneoussolncoeffs(C[i], sigmat, sigmas,g,)
    
    radiance=0
        
    for j in range(3):
        for i in range(3):
            radiance+=C[i]*np.exp(B[i,4]*r)*(2*i+1)*B[j,i]*scipy.special.legendre(i)(mu)
        for k in range(3):
            radiance+=A[k]*(2*k+1)*np.exp(sigmat*r)*scipy.special.eval_legendre(k, mu)
            
    return radiance
        










