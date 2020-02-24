#  Code written by Jerin Rajan on 27th Jan 2019

# Function to calculate Mass (kg/m3) and Cost (£/kg)
# Inputs: l = length, b = breadth, h=height
# Outpts: mass = mass of the solution.
# To keep the algorithm simple we will only return the cost for now.

def mass(l,b,h):
    density = round(float(9.77/1000),2)
    costmat = round(float(1.30),2)
    mass = round(float(l*b*h*density),2)
    cost = round(float(mass*costmat),2)

    return cost
