# The code executes mathimatical Operations on a vaild Elliptic Curve.

class EllipticCurve:

    def __init__(self, a: int, b: int, p:int):
        self.a: int = a
        self.b: int = b
        self.p: int = p

    def calculatesPointsOnElipticcurve(self: object) -> list:
        ListOfPointsOnCurve = []
        for x in range(0, EC.p):
            for y in range(0, EC.p):
                if (y ^ 2) % EC.p == (x ^ 3 + EC.a * x + EC.b) % EC.p:
                    ListOfPointsOnCurve.append((x, y))
        return ListOfPointsOnCurve

    def givesOrderOfEllipticcurve(ListOfPointsOnCurve: list) -> int:
        a = list.size()
        return a


class Point:
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y

    def checksIfPointOnCurve(self: object, EC: object) -> bool:
        if (self.y ^ 2) % EC.p == (self.x ^ 3 + EC.a * self.x + EC.b) % EC.p:
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
    

def doubleThePoint(EC, P):
    firsthalf = (3 * P.x ^ 2 + EC.a) % EC.p
    seconedhalf = (2 * P.y * 1) % EC.p
    s = firsthalf * advencedEuclidAlgorithm(EC.p, seconedhalf) % EC.p


def advencedEuclidAlgorithm(x: int, y: int) -> int:
    ggTSteps = ggT(x, y)


def ggT(x: int, y: int) -> list:
    ggTSteps = [x, y]
    if x >= y and y != 0:
        z = x % y
        z.append(z)
        ggT(y, z)
    return ggTSteps



EC = EllipticCurve(3, 6, 17)
P = Point(1, 17)
Q = Point(3, 9)
print(P.checksIfPointOnCurve(EC))
print(definesOperationToDo(EC, P, Q))