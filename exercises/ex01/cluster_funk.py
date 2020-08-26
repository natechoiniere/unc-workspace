"""This program evaluates the rate of change in infection cluster size given an initial infected population,
as well as a value for the contagiousness of the disease."""

__author__ = "730443739"

contagionIndex: str = input("Enter R0: ") # R0, as a string
initPop: str = input("Enter t0 Cluster Size: ") # Population of infected

newCaseNum1: float = float(initPop) * float(contagionIndex)
totalCaseNum1: float = newCaseNum1 + float(initPop)

newCaseNum2: float = float(newCaseNum1) * float(contagionIndex)
totalCaseNum2: float = totalCaseNum1 + newCaseNum2

newCaseNum3: float = float(newCaseNum2) * float(contagionIndex)
totalCaseNum3: float = totalCaseNum2 + newCaseNum3

newCaseNum4: float = float(newCaseNum3) * float(contagionIndex)
totalCaseNum4: float = totalCaseNum3 + newCaseNum4


print("t1 - New: " + str(round(newCaseNum1)) + " - Total: " + str(round(totalCaseNum1)))
print("t2 - New: " + str(round(newCaseNum2)) + " - Total: " + str(round(totalCaseNum2)))
print("t3 - New: " + str(round(newCaseNum3)) + " - Total: " + str(round(totalCaseNum3)))
print("t4 - New: " + str(round(newCaseNum4)) + " - Total: " + str(round(totalCaseNum4)))
