# Case1: cos(theta) = 1
def calibrate(n1, n2, A, alpha):
    
    if n1 > n2:
        print("Exitting n1 > n2")
        return None 
        exit()

#     A, alpha = symbols("A alpha")
        
    theta_c = math.acos((n1 + 0.0)/(n2 + 0.0))
    theta_c_deg = math.degrees(theta_c)
    
    symbolic_approx_reflectance_1 = approx_reflectance(0.0, theta_c_deg, A, alpha )
    print(symbolic_approx_reflectance)
    
    a_temp = 0.25 + 0.75 * math.cos(theta_c)
    theta_1 = math.acos(a_temp)
    theta_1_deg = math.degrees(theta_1)
    
    symbolic_approx_reflectance_2 = approx_reflectance(theta_1_deg, theta_c_deg, A, alpha )
# Case1: cos(theta) = 1
    LHS_1 = reflectance(n1, n2, 1.0)
    RHS_1 = symbolic_approx_reflectance_1
    
# Case2: cos(theta) = 0.25 + 0.75 * cos(theta_c)
    LHS_2 = reflectance(n1, n2, math.cos(theta_1))
    RHS_2  = symbolic_approx_reflectance_2
    
"""
Here RHS_1, RHS_2 were unused, could possibly employed in getting down solutions from optimisers from sympy/scipy.
"""
    temp = math.sqrt( 1.0 - (n1 + 0.0)/(n2 + 0.0) )
    
    alpha= math.log( (LHS_1+0.0)/(LHS_2+0.0) ) * 2.0 / (temp)  
    
    A = (LHS_1 - 1.0) / ( (exp(b*temp) - 1 ) 
    return alpha, A 
