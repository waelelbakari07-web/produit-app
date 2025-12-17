while True:
    X = int(input("entrez le premier nombre positif : "))
    Y = int(input("entrez le deuxieme nombre positif : "))
    if (X > 0) and (Y > 0):
        break
if (X == 0) or (Y == 0):
    P = 0
else:
    if (X > Y):
        P = 0
        for i in range (1,Y + 1):
            P = P + X
    else:
        P = 0 
        for i in range (1,X + 1):
            P = P + Y
print("le produit est " ,P)
