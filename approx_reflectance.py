def approx_reflectance(theta_c_deg, theta_deg, A, alpha):
    
    
    theta_c = math.radians(theta_c_deg)
    theta = math.radians(theta_deg)
    
    if math.cos(theta) < math.cos(theta_c):
        return 1.0;
    
    inside_sqrt = math.cos(theta) - math.cos(theta_c)
    print("inside_sqrt", inside_sqrt)
    inside_exp = alpha * math.sqrt(inside_sqrt) 
    print("inside_exp", inside_exp)
    left_of_one = exp( inside_exp )
    print("left_of_one", left_of_one)
    
    
    final_form = 1.0 + A * (left_of_one - 1.0)
    
    return final_form;
