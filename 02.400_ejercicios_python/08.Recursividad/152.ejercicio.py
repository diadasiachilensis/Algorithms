def countdown(n):
    if n<=0:
        return 0
    else:
        print(n)
        countdown(n-1) 

countdown(10)