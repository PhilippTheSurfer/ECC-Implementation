# The code executes mathimatical Operations on a vaild Elliptic Curve.

class EllipticCurve:
    a: int
    b: int
    p: int

    def calculatesPointsOnElipticcurve(EC: object) -> list:
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
    x: int
    y: int

    def checksIfPointOnCurve(EC: object, P: object) -> bool:
        if (P.y ^ 2) % EC.p == (P.x ^ 3 + EC.a * P.x + EC.b) % EC.p:
            return True
        else:
            return False

    def calculatesOrderOfPoint(EC: object, P: object) -> int:
        # calculates Foobar
        return None


EC = EllipticCurve(3, 6, 17)
P = Point(1, 17)
print(EC.a)
