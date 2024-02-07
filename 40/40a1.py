n=int(input("enter a number"))
k=int(input("enter position"))


def res(n,k):
    factor=[]


    for i in range(1,n+1):
        if n%i==0:
            factor.append(i)
    factor.sort(reverse=True)

    if k<=len(factor):
        ans=factor[k-1]
        print(f"the {k} th largest element of {n} is {ans}")
    else:
        print("invalid position")    


res(n,k)