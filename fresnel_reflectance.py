def reflectance(n1, n2, c):
#     c =  3.0e8
   

    M1 = n1 * sqrt(1 - (n1/n2 * sqrt(1-c**2))**2);
#     print("M1:")
#     print(M1)

    M2 = n2 * sqrt(1 - (n1/n2 * sqrt(1-c**2))**2);
#     print("M2:")
#     print(M2)


    Rs = ((n1*c - M2)/(n1*c + M2))**2;
    print("Rs:")
    print(Rs)

    Rp = ((n2*c - M1)/(n2*c + M1))**2;
    print("Rp:")
    print(Rp)

    
    Reff = 0.5 * (Rs + Rp);
#     print("Reff:")
#     print(Reff)


    
    return Reff;
