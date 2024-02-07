str=input("enter string")
str_low=str.lower()
search="india"
i=0
while i<len(str_low):
    oi=str_low.find(search,i)
    if oi==-1:
        break
    print("found india at",oi)
    i=oi+1