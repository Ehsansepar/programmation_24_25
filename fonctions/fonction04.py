def indexMax(serie):
    maxi = serie[0]
    index = 0
    
    print("\nindex | Nbr")

    for i in range(len(serie)) : 
        print(f"{i:5} | {serie[i]}")
        if serie[i] > maxi :
            maxi = serie[i]
            index = i 

    return f"\nGrand nombre est {maxi} | index {index}"


serie = [5, 8, 2, 1, 9, 3, 6, 7]
serie2 = [-5, -1, -7, -9]
print(indexMax(serie2)) # affichera 4.