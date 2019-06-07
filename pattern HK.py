n=9
l=1
p=1
for i in range(1,n+1):
    for j in range(1,(n+n//2)+1):
        if j==1 or j==n:
            print("*",end="")
        if (j!=1 and j!=n) and i!=n//2+1:
            print(" ",end="")
        if i==n//2+1 and j<=n:
            if j!=n:
                print("*",end="")
            else:
                print(" ",end="")
        if j==n:
            print("*",end="")
        if j>n and i<=n//2+1:
            if j==n+n//2+1-l:
                print("*",end="")
            else:
                print(" ",end="")
        if j>n and i>n//2+1:
            if j==n+p:
                print("*",end="")
            else:
                print("",end="")
    l=l+1
    if i>n//2+1:
        p=p+1
    print("")