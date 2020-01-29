
def mass(l,b,h):
    density = round(float(9.77/1000),2)
    costmat = round(float(1.30),2)
    mass = round(float(l*b*h*density),2)
    cost = round(float(mass*costmat),2)

    return mass,cost
