str=input("enter string")
str_low=str.lower()
search="emma"
lp=-1
i=0
while i<len(str_low):
    oi=str_low.find(search,i)
    if oi==-1:
        break
    lp=oi
    i=oi+1
if lp!=-1:
    print(lp)
else:
    print("not found")        