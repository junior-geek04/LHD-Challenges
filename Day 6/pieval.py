import math 

def CalculatePi(roundVal):

		somepi = round(math.pi,roundVal)
		pi = str(somepi)
		someList = list(pi)
		return somepi
roundTo = input("Enter the number of digits :")

roundint = int(roundTo)
print(CalculatePi(roundint))
