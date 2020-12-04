#!/home/valentin/.anaconda3/bin/python

from Pret import *

testPret = Pret(355000, 0.013, 25, 0.003)

testPret.build()
print(testPret)
# testPret.graph()
testPret.graph2()
