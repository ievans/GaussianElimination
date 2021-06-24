# Copyright (c) Isaac Evans 2011
# All rights reserved.

# Tests for the guassian elimination code
# Note that the result strings coded in 
# may not exactly match the output on your
# system due to differences in floating-point
# precision.
from gaussianelimination import myGauss

# these first two tests integrate into my symbolic calculator
#print myGauss([[S('x'),2.0,6.0],
#               [2.0,6.0,0]])
#print myGauss([[S('M') * S('x'),S('b'),S('y')],
#               [2.0,6.0,0]])

print myGauss([[-3.0,2.0,-6.0,6.0],
               [5.0,7.0,-5.0,6.0],
               [1.0,4.0,-2.0,8.0]])
print '[-2.0, 3.0, 1.0]'
print

print str(myGauss([[2.0,4.0,6.0,8.0,10.0,0.0],
               [1.0,3.0,5.0,8.0,3.0,-1.0],
               [3.0,8.0,9.0,20.0,3.0,5.0],
               [4.0,8.0,9.0,-2.0,3.0,8.0],
               [5.0,-3.0,3.0,-2.0,1.0,0]]))
print '[1.8835063437139565, 1.7012687427912341, -1.4160899653979238, -0.050749711649365627, -0.16695501730103807]'
print
# examples from http://en.wikipedia.org/wiki/Gaussian_elimination
print myGauss([[2.0,1.0,-1.0,8.0],
               [-3.0,-1.0,2.0,-11.0],
               [-2.0,1.0,2.0,-3.0]])
print '[2.0, 3.0, -1.0]'
print
print x == x

print myGauss([[1.0,4.0,-2.0,8.0],
               [5.0,7.0,-5.0,6.0],
               [-3.0,2.0,-6.0,6.0]])
print '[-2.0, 3.0, 0.9999999999999996]'
