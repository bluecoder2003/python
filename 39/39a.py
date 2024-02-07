str=input("enter string: ")
str_l=str.lower()
vowels=['a','e','i','o','u']
for element in str_l:
    if element in vowels:
        vowels.remove(element)
size=len(vowels)        
if size==0:
    print(f"accepted {str}")
else:
    print("rejected")    