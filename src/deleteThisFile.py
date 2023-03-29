#

from calculate_on_ECC import EllipticCurve
import math


def advencedEuclidAlgorithm(EC: object, x: int, y: int) -> int:
    qi = ggT(x, y)
    print("This is ggT: " + str(qi))
    ri = []
    ti = [0, 1]
    for i in range(len(qi) - 2):
        ri.append(math.floor(qi[i] / qi[i+1]))
    print("This is ri:  " + str(ri))
    for i in range(len(ri)):
        ti.append(ti[i] - ti[i+1] * ri[i])
    print("This is ti:  " + str(ti))
    while ti[len(ti)-1] <= 0:
        ti[len(ti)-1] = ti[len(ti)-1] + EC.p
    print(ti[len(ti)-1])
    return ti[len(ti)-1]


def ggT(x, y) -> list:
    ggTSteps = []
    ggTSteps.append(x)
    ggTSteps.append(y)
    while x >= y and y != 0:
        z = x % y
        ggTSteps.append(z)
        x = y
        y = z
    return ggTSteps

#    if x >= y and y != 0:
#        z = x % y
#        ggTSteps.append(z)
#        ggT(y, z)
#    print(ggTSteps)
#    return ggTSteps


EC = EllipticCurve(2, 2, 17)
x = 19
y = 17
advencedEuclidAlgorithm(EC=EC, x=x, y=y)
print(__name__)