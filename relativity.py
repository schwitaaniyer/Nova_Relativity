#Code for Formulas in Relativity

global c
c = 2.9*(10**8)

def e_mc2(m):
    E = m*(c**2)
    return E

def length_contraction(l,v):
    rl = l*((1-((v**2)/(c**2)))**0.5)
    return rl

def relativistic_kinetic_energy(m,v):
    rKE = 0.5*m*(v**2)
    return rKE

def time_dilation(t,v):
    rt = t/((1-((v**2)/(c**2)))**0.5)
    return rt

def velocity_addition(v,w):
    u = (v+w)/(1+(v*w)/(c**2))
    return u

def mass_variation(m,v):
    rm = m/((1-((v**2)/(c**2)))**0.5)
    return rm   