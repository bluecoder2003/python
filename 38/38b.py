n=int(input("enter the size: "))
l=[]
print("enter the elements \n")

for i in range(1,n+1):
    element=int(input())
    l.append(element)
print(f"original array \n {l}")  

def bubble_sort(l):
    for i in range(0,n-2):
        for j in range(0,n-i-1):
            if(l[j] > l[j+1]):
                temp=l[j]
                l[j]=l[j+1]
                l[j+1]=temp
    return l            

new_l=bubble_sort(l)
print(f"after sorting \n {new_l}")