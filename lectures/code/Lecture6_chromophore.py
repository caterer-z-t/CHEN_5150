def chromophore(t, y):
    import numpy as np
    # solving a non-stiff ODE using the toy receptor-complex model given in the lecture notes.
    # Inputs:
        # t - a 1 x n time vector.
        # y - a n x 4 concentration vector of unfolded, folded, cyclized and oxidized GFP.
    # Output:
        # dydt - a n x 4 vector of the rate of production of of unfolded, folded, cyclized and oxidized GFP.
    
    k1 = 0.069
    k2 = 0.231
    k3 = 0.0091
    growth_rate = 0.00462
    
    # all kinetic constants are in units of inverse minutes.
    dydt = np.zeros(4)
    dydt[0] = 1 - (k1 + growth_rate)*y[0]  # dydt[1] is for U/X in units of nM/gDCW
    dydt[1] = k1*y[0] - (k2 + growth_rate)*y[1]    # dydt[2] is for F/X in units of nM/gDCW
    dydt[2] = k2*y[1] - (k3 + growth_rate)*y[2]    # dydt[3] is for FC/X in units of nM/gDCW
    dydt[3] = k3*y[2] - growth_rate*y[3]   # dydt[4] is for FO/X in units of nM/gDCW
    return dydt