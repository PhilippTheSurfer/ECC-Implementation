import sys
import os
import pytest
from sympy import isprime

# Add the parent folder to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src import calculate_on_ECC as ECC


def test_check_If_Point_is_On_Curve():
    ec = ECC.EllipticCurve(12, 4, 23)

    p = ECC.Point(0, 2)
    assert(p.checksIfPointOnCurve(ec=ec))

    p = ECC.Point(6, 19)
    assert(p.checksIfPointOnCurve(ec=ec))


def test_check_If_Point_Is_Not_On_Curve():
    ec = ECC.EllipticCurve(12, 4, 23)

    p = ECC.Point(2, 18)
    assert(not p.checksIfPointOnCurve(ec=ec))

    p = ECC.Point(14, 9)
    assert(not p.checksIfPointOnCurve(ec=ec))

    

def test_detact_prime_correctly():
    assert(isprime(23))


def test_detact_nonprime_correctly():
    assert(False == isprime(22))

    #
    #pytest: param
    #    viele Punkte die druchgetestet werden.
    #