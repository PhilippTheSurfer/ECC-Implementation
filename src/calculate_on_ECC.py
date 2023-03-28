# The code executes mathimatical Operations on a vaild Elliptic Curve.

import math


class EllipticCurve:

    def __init__(self, a: int, b: int, p:int):
        self.a: int = a
        self.b: int = b
        self.p: int = p

    def calculatesPointsOnElipticcurve(self: object) -> list:
        ListOfPointsOnCurve = []
        for x in range(0, EC.p):
            for y in range(0, EC.p):
                if (y ** 2) % EC.p == (x ** 3 + EC.a * x + EC.b) % EC.p:
                    ListOfPointsOnCurve.append((x, y))
        return ListOfPointsOnCurve

    def givesOrderOfEllipticcurve(ListOfPointsOnCurve: list) -> int:
        a = len(ListOfPointsOnCurve)
        return a


class Point:
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y

    def checksIfPointOnCurve(self: object, EC: object) -> bool:
        if (self.y ** 2) % EC.p == (self.x ** 3 + EC.a * self.x + EC.b) % EC.p:
            return True
        else:
            return False

    def calculatesOrderOfPoint(EC: object, P: object) -> int:
        # calculates Foobar
        return None


def definesOperationToDo(EC: object, P: object, Q: object) -> bool:
    if P.x % EC.p == Q.x % EC.p and P.y % EC.p == Q.y % EC.p:
        return True
    else:
        return False
    

def addThePoint(EC: object, P:object, Q: object) -> tuple:
    firsthalf = (Q.y - P.y) % EC.p
    secondhalf = (Q.x - P.x)
    s = firsthalf * advencedEuclidAlgorithm(EC.p, secondhalf) % EC.p
    x_3 = (s ** 2 - P.x - P.x) % EC.p
    y_3 = (s * (P.x - x_3) - P.y) % EC.p
    print("The sum of P and Q on the ElliptivCurve: y^2 = x^3 + " + str(EC.a) + "*x + " + str(EC.b) + " mod " + str(EC.p) + " is: \n" " 2P = (" + str(x_3) + ", " + str(y_3) + ")")



def doubleThePoint(EC: object, P: object):
    firsthalf = (3 * P.x ** 2 + EC.a) % EC.p
#    print("firsthalf of s: " + str(firsthalf))
    secondhalf = (2 * P.y * 1)
#    print("secondhalf of s: " + str(secondhalf))
    s = firsthalf * advencedEuclidAlgorithm(EC.p, secondhalf) % EC.p
#    print("This is s: " + str(s))
    x_3 = (s ** 2 - P.x - P.x) % EC.p
    y_3 = (s * (P.x - x_3) - P.y) % EC.p
    print("The double of the given Point on the ElliptivCurve: y^2 = x^3 + " + str(EC.a) + "*x + " + str(EC.b) + " mod " + str(EC.p) + " is: \n" " 2P = (" + str(x_3) + ", " + str(y_3) + ")")


def advencedEuclidAlgorithm(x: int, y: int) -> int:
    """solves ax + b·y = ggT(a;b) with a, b = N (neben dem ggT(a;b) as
    one step) the solution: x, y
    Calculates the inverse of a given number

    Args:
        x (int): first redueced number and primmodulo of Elliptic curve
        y (int): modulo of ggT

    Returns:
        int: gives the inverse of the input number
    """
    qi = ggT(x, y)
#    print("This is ggT: " + str(qi))
    ri = []
    ti = [0, 1]
    for i in range(len(qi) - 2):
        ri.append(math.floor(qi[i] / qi[i+1]))
#    print("This is ri:  " + str(ri))
    for i in range(len(ri)):
        ti.append(ti[i] - ti[i+1] * ri[i])
#        print(str(ti[i]) +  "-" + str(ti[i+1]) + "*" + str(ri[i]) + "=" + str(ti[i] - ti[i+1] * ri[i]))
#    print("This is ti:  " + str(ti))
    while ti[len(ti)-1] <= 0:
        ti[len(ti)-1] + x
#    print(ti[len(ti)-1])
    return(int(ti[len(ti)-1]))


def ggT(x: int, y: int) -> list:
    ggTSteps = []
    ggTSteps.append(x)
    ggTSteps.append(y)
    while x >= y and y != 0:
        z = x % y
        ggTSteps.append(z)
        x = y
        y = z
    return ggTSteps


def main(EC: object, P: object, Q: object):
    """
        Add a workflow for the code 
    """


EC = EllipticCurve(2, 2, 17)
P = Point(7, 6)
Q = Point(3, 5)

addThePoint(EC, P, Q)