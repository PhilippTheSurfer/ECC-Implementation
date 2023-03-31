import sys
import os

# Add the parent folder to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src import calculate_on_ECC as ECC


def test():
    ec = ECC.EllipticCurve(12, 4, 23)
    P = ECC.Point(0, 2)
    if P.checksIfPointOnCurve(ec=ec):
        print("valid")
    else:
        print("false")


test()

def test_2():
    ec = ECC.EllipticCurve(12, 4, 22)
    P = ECC.Point(0, 5)
    if P.checksIfPointOnCurve(ec=ec):
        print("valid")
    else:
        print("false")


test_2()
    #
    #pytest: param
    #    viele Punkte die druchgetestet werden.
    #