def pow(n,e):
    if e==0:
        return 1
    else:
        n*pow(n,e-1)

print(pow(2,3))