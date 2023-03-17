#!/opt/anaconda3/bin/python

from Pret import *

testPret = Pret(300000, 0.02, 25)

testPret.build()
print(testPret)
testPret.graph2()
