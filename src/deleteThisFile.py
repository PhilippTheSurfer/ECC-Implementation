def advencedEuclidAlgorithm(x: int, y: int) -> int:
    ggTSteps = ggT(x, y)
    print(ggTSteps)

def ggT(x, y) -> list:
    ggTSteps = [x, y]
    if x >= y and y != 0:
        z = x % y
        ggTSteps.append(z)
        ggT(y, z)
    print(ggTSteps)
    return ggTSteps


x = 19
y = 17
advencedEuclidAlgorithm(x, y)