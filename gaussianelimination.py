# Copyright (c) Isaac Evans 2011
# All rights reserved.

def myGauss(m):
    # eliminate columns
    for col in range(len(m[0])):
        for row in range(col+1, len(m)):
            r = [(rowValue * (-(m[row][col] / m[col][col]))) for rowValue in m[col]]
            m[row] = [sum(pair) for pair in zip(m[row], r)]
    # now backsolve by substitution
    ans = []
    m.reverse() # makes it easier to backsolve
    for sol in range(len(m)):
            if sol == 0:
                ans.append(m[sol][-1] / m[sol][-2])
            else:
                inner = 0
                # substitute in all known coefficients
                for x in range(sol):
                    inner += (ans[x]*m[sol][-2-x])
                # the equation is now reduced to ax + b = c form
                # solve with (c - b) / a
                ans.append((m[sol][-1]-inner)/m[sol][-sol-2])
    ans.reverse()
    return ans

def runTests():
    # these first two tests integrate into my symbolic calculator
    print myGauss([[S('x'),2.0,6.0],
               [2.0,6.0,0]])
    print myGauss([[S('M') * S('x'),S('b'),S('y')],
               [2.0,6.0,0]])

    print myGauss([[-3.0,2.0,-6.0,6.0],
               [5.0,7.0,-5.0,6.0],
               [1.0,4.0,-2.0,8.0]])

    print str(myGauss([[2.0,4.0,6.0,8.0,10.0,0.0],
               [1.0,3.0,5.0,8.0,3.0,-1.0],
               [3.0,8.0,9.0,20.0,3.0,5.0],
               [4.0,8.0,9.0,-2.0,3.0,8.0],
               [5.0,-3.0,3.0,-2.0,1.0,0]])) == '[1.8835063437139565, 1.7012687427912341, -1.4160899653979238, -0.050749711649365627, -0.16695501730103807]'

    # examples from Wikipedia
    print myGauss([[2.0,1.0,-1.0,8.0],
               [-3.0,-1.0,2.0,-11.0],
               [-2.0,1.0,2.0,-3.0]])
    print myGauss([[1.0,4.0,-2.0,8.0],
               [5.0,7.0,-5.0,6.0],
               [-3.0,2.0,-6.0,6.0]])
