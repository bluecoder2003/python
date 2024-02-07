l=[5,6,3,8,9,2]

def max_min(l):
    maxi=-1
    mini=999
    max_index=0
    min_index=0
    for i in range (0,len(l)):
        if maxi<=l[i]:
            maxi=l[i]
            max_index=i
        if mini>=l[i]:
            mini=l[i]
            min_index=i
    print(f"max number is {maxi} at index {max_index}")        
    print(f"max number is {mini} at index {min_index}")   

max_min(l)         

    