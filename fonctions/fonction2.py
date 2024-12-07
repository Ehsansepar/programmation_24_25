def intComp(cd, t, n):
    cf = cd * (1 + t) ** n
    return cf

print(round(intComp(10000,0.01,20), 3))
