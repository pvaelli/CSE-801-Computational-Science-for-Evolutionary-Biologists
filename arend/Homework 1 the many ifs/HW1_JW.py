#!/usr/bin/python2.7
import random, numpy
# generate random numbers
a = random.randint(0,2)
b = random.randint(0,3)
# math way
diffs = abs(a-b)
print ("a = %s \nb = %s" % (a, b))
print ("|a - b| = %s" % diffs)

# not using math way
if (a == b):
    print "Zero difference"
elif (a > b):
    if (a == 2) and (b == 0):
        print "Two differences"
    else:
        print "One difference"
else:
    if (a==0) and (b==3):
        print "Three differences"
    elif (b==2 and a ==0) or (a==1 and b==3):
        print "two differences"
    else:
        print "one difference"
