# Code written by Jerin Rajan on 27th Jan 2019

import random
from masscost import mass


size_of_tl = 10
i = 0;
# X - set of feasible solutions
# Dimension of our metal plate (in mm) l: length, b: breadth, h: height
l = 100
b = 50
h = 15
X = [l,b,h]
mass_X, cost_X = mass(l,b,h)
print('Mass of the item:', mass_X)
print('Cost of metal:', cost_X)

# defining a tabu list
tl = list()

# Step0
# Initialising tabu list to empty
tl = []
# Aspiration criteria to be Zero
ac = 0

#Step1
# Set Iteration counter
k = True

# Initial Solution - generated randomly
# xl = random.randint(0,l)
# xb = random.randint(0,b)
# xh = random.randint(0,h)
# print('Random dimensions:',xl,xb,xh)
x = [random.randint(0,l),random.randint(0,b),random.randint(0,h)]
print('Random dimensions:',x[0],x[1],x[2])

while k is True:
    xb = x

    # Step2:
    # Trial solutions in neighbourhood
    sneigh = [[x[0]-1,x[1],x[2]],[x[0]+1,x[1],x[2]],[x[0],x[1]-1,x[2]],[x[0],x[1]+1,x[2]],[x[0],x[1],x[2]-1],[x[0],x[1],x[2]+1]]
    print('Trial Solutions:',sneigh)

    for i in range(len(sneigh)):
        xnb = sneigh[i][0],sneigh[i][1],sneigh[i][2]
        print('xnb values:',xnb)
        e_xnb = mass(sneigh[i][0],sneigh[i][1],sneigh[i][2])
        print('e_xnb:',e_xnb)
        print('xb values:',xb[0],xb[1],xb[2])
        e_xb = mass(xb[0],xb[1],xb[2])
        print('e_xb:',e_xb)
    # Step 3 - comparing the objective functions
        if e_xnb < e_xb:
            xb = xnb
            print('new xb:',xb)
    # Step 4 - Perform the Tabu test
        else:
            print('Go to step 4 perform tabu test')
            if xnb not in tl:
                # Accept xnb as current solution
                x = xnb
                # Update TL
                tl.append(xnb)
                # Update AC
                # print('Tabu List:',tl)
                # Step 6 - Perform termination test.
                print('Go to Step 6, Perform terminatation test')
                length_tl = len(tl)
                if length_tl < size_of_tl:
                    k = True
                else:
                    k = False
                    break
# Step 5 Perform the AC test
            else:
                print('Go to Step 5 - Perform AC test')
                

best_sol = tl[size_of_tl-1]
print('Tabu List:',tl)
print('Best Solution:', best_sol)
print('Cost:', mass(best_sol[0],best_sol[1],best_sol[2]))
