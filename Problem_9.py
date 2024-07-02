for a in range (1, 501):
    for b in range (1, 501):
        for c in range (1, 501):
            if a**2+b**2==c**2 and a<b<c and a+b+c==1000:
                print(a*b*c)