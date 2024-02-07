#task1
s=input("Enter a string: ")
new=s[1:-1]
print(new)

#task2
s1=input("Enter a string: ")
s2=input("Enter a string: ")

first=s1[0]+s2[0]
middle=s1[len(s1)//2]+s2[len(s2)//2]
last=s1[-1]+s2[-1]

print(first+middle+last)

#task3
s3=input("Enter a string: ")
s4=input("Enter a string: ")
mid=len(s3)//2
r=s3[:mid]+" "+s4+" "+s3[mid:]
print(r)

