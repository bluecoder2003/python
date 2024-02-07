x=int(input("enter number of items"))
if x<10:
    print(x*120)
elif x>=10 and x<=99:
    print(x*100)
elif x>=100:
    print(x*70)
else:
	print("Invalid number of items bought")            