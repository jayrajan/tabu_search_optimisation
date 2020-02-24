import random
from masscost import mass

# Sample Data Set
# X - set of feasible solutions
# Dimension of our metal plate (in mm) l: length, b: breadth, h: height
l = 100
b = 50
h = 15
X = [l,b,h]
cost_X = mass(l,b,h)
print('Cost of metal:', cost_X)

# defining a tabu list
tl = list()
# For loop iteration item handler initialisation
i = 0;
# Maximium size of the Tabu list
max_tl = 10
# Cost Function threhdold
cost_threshold = 50


#Step1
# Set Iteration counter
k = 0

# Initial Solution - generated randomly - assuming best solution seen to date.
s0 = [random.randint(1,l),random.randint(1,b),random.randint(1,h)]
print('Random dimensions:',s0[0],s0[1],s0[2])
# Best Mass value initialisation
best_mass = mass(s0[0],s0[1],s0[2])
# best_mass =
print('Initial Best mass:',best_mass)


sbest = s0
bestCandidate = s0

# Initialising the tabu list with x
tl.append(s0)

while not (k == 20 ):
# Step2:
# Trial solutions in neighbourhood (Candidate List)
    s0 = sbest
    sneigh = [[s0[0]-1,s0[1],s0[2]],[s0[0]+1,s0[1],s0[2]],
            [s0[0],s0[1]-1,s0[2]],[s0[0],s0[1]+1,s0[2]],
            [s0[0],s0[1],s0[2]-1],[s0[0],s0[1],s0[2]+1]]
    print('Trial Solutions:',sneigh)

    for i in range(len(sneigh)):
        # if sneigh[i][0] <= 0:
        #     continue
        # elif sneigh[i][1] <= 0:
        #     continue
        # elif sneigh[2] <= 0:
        #     continue

        sCandidate = sneigh[i][0],sneigh[i][1],sneigh[i][2]
        print('sCandidate:',sCandidate)

        if sCandidate[0]<=0:
            continue
        elif sCandidate[1]<=0:
            continue
        elif sCandidate[2]<=0:
            continue
        else:
            e_sCandidate = mass(sCandidate[0],
                    sCandidate[1],sCandidate[2])
            print('e_sCandidate:',e_sCandidate)
            print('bestCandidate:',bestCandidate[0],
                    bestCandidate[1],bestCandidate[2])
            e_bestCandidate = mass(bestCandidate[0],
                    bestCandidate[1],bestCandidate[2])
            print('e_bestCandidate:',e_bestCandidate)
            # Tabu Test
            if (not sCandidate in tl) and (e_sCandidate < e_bestCandidate):
                bestCandidate = sCandidate
                print('bestCandidate:',bestCandidate)

    e_sbest = mass(sbest[0],sbest[1],sbest[2])
    print('e_sbest:',e_sbest)

    # Acceptance Criterion Test
    if e_bestCandidate < e_sbest:
        sbest = bestCandidate
        best_mass = mass(sbest[0],sbest[1],sbest[2])
        print('sbest:',sbest)
        print('sbestMass:', best_mass)

    tl.append(sbest)
    print('tl:',tl)
    if len(tl)>max_tl:
        tl.pop(0)
    k = k+1
print("Optimal Candidate:",sbest)
print("optimalCost", best_mass)
