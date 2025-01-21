def maximum(n1, n2, n3) : 
    lst = [n1, n2, n3]

    maxi = -1000000000

    for i in range(len(lst)) : 
        if lst[i] > maxi :
            maxi = lst[i]
    
    return maxi

print(maximum(-1, -2, -5))