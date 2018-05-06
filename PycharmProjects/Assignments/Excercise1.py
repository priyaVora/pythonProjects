import math
"""Developing in Third Party Framework
    Priya Vora
    5/4/2018
    E=mc ^2
"""
c = math.pow(100,4) * 3

m = input("Supply a number for mass: ")

floatValue = float(m)
cSquared = math.pow(c, 2)

calculation = (floatValue * float(cSquared))
e = float(calculation)


print("\nMass: %s" % m)
print("Energy = %e" % e)