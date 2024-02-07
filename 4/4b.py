str=input("enter string")
def remove(str):
    unique=set()
    ans=""
    for element in str:
        if element not in unique:
            unique.add(element)
            ans +=element
    return ans        
res=remove(str)
print(res)