# The code executes mathimatical Operations on a vaild Elliptic Curve.

import math
from sympy import isprime

class EllipticCurve:

    def __init__(self, a: int, b: int, p: int):
        if not isprime(p):
            raise ValueError("p is not prime.")
        if not ((4 * a ** 3) + (27 * b ** 2)) % p != 0:
            raise ValueError("a,b,p do not meet ECC equation Requirement")
        self.a: int = a
        self.b: int = b
        self.p: int = p


    def calculatesPointsOnElipticcurve(self) -> list:
        ListOfPointsOnCurve = []
        for x in range(0, self.p):
            for y in range(0, self.p):
                if (y ** 2) % self.p == (x ** 3 + self.a * x + self.b) % self.p:
                    ListOfPointsOnCurve.append((x, y))
        return ListOfPointsOnCurve

    def givesOrderOfEllipticcurve(ListOfPointsOnCurve: list) -> int:
        a = len(ListOfPointsOnCurve)
        return a


class Point:
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y

    def checksIfPointOnCurve(self, ec: EllipticCurve) -> bool:
        if (self.y ** 2) % ec.p == (self.x ** 3 + ec.a * self.x + ec.b) % ec.p:
            return True
        else:
            print("The Point provided is not on the Curve")
            return False

    def calculatesOrderOfPoint(self) -> int:
        count = 1
        T = p
        while not Point.isInfinityPoint(T):
            T = p + T
            count += 1
        return count

    def isInfinityPoint(self) -> bool:
        if p.x is None and p.y is None:
            return True
        else:
            return False


def pointsEqual(ec: EllipticCurve, p: Point, q: Point) -> bool:
    if p.x % ec.p ==   q.x % ec.p and p.y % ec.p ==   q.y % ec.p:
        return True
    else:
        return False


def addThePoint(ec: EllipticCurve, p: Point,  q: Point) -> tuple:
    firsthalf = (  q.y - p.y) % ec.p
    secondhalf = ( q.x - p.x)
    s = firsthalf * advencedEuclidAlgorithm(ec.p, secondhalf) % ec.p
    x_3 = (s ** 2 - p.x - p.x) % ec.p
    y_3 = (s * (p.x - x_3) - p.y) % ec.p
    print("The sum of p and    q on the ElliptivCurve: y^2 = x^3 + " + str(ec.a) + "*x + " + str(ec.b) + " mod " + str(ec.p) + " is: \n" " 2P = (" + str(x_3) + ", " + str(y_3) + ")")


def doubleThePoint(ec: EllipticCurve, p: Point) -> tuple:
    firsthalf = (3 * p.x ** 2 + ec.a) % ec.p
#    print("firsthalf of s: " + str(firsthalf))
    secondhalf = (2 * p.y * 1)
#    print("secondhalf of s: " + str(secondhalf))
    s = firsthalf * advencedEuclidAlgorithm(ec.p, secondhalf) % ec.p
#    print("This is s: " + str(s))
    x_3 = (s ** 2 - p.x - p.x) % ec.p
    y_3 = (s * (p.x - x_3) - p.y) % ec.p
    print("The double of the given Point on the ElliptivCurve: y^2 = x^3 + " + str(ec.a) + "*x + " + str(ec.b) + " mod " + str(ec.p) + " is: \n" " 2P = (" + str(x_3) + ", " + str(y_3) + ")")


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
        ti[len(ti)-1] = ti[len(ti)-1] + x
#    print(ti[len(ti)-1])
    return int(ti[len(ti)-1])


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


def main(ec: EllipticCurve, p: Point,    q: Point):
    """
        Add a workflow for the code
    """


if __name__ == "__main__":
    ec = EllipticCurve(2, 2, 17)
    p = Point(7, 6)
    q = Point(3, 5)
    p.checksIfPointOnCurve(ec)

    print(__name__)
