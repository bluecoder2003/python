a=int(input("enter side"))
b=int(input("enter side"))
c=int(input("enter side"))
if a==b==c:
    print("equilateral")
elif a!=b and b!=c and c!=a:
    print("scalene")
else:
    print("isoceles")    