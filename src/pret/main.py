#!/home/valentin/.anaconda3/bin/python

from Pret import *

testPret = Pret(200000, 0.0185, 20, 0.008)

testPret.build()
print(testPret)
# testPret.graph()
testPret.graph2()
