import os
print(os.path)
# import .src.calculate_on_ECC as ECC
#from src import calculate_on_ECC as ECC

def test():
    EC = ECC.EllipticCurve(12, 4, 23)
    P = ECC.Point(0, 2)
    if P.checksIfPointOnCurve(EC=EC):
        print("valid")
    else:
        print("false")
