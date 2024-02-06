# Given two sorted lists, merge them into one list which should also be sorted. Implement the solution in Python and see if your code runs successfully.

def mergeLists(lst_a,lst_b):
    index_a = 0
    index_b = 0
    while(index_a<len(lst_a) and index_b < len(lst_b)):
        if(lst_a[index_a] > lst_b[index_b]):
            lst_a.insert(index_a,lst_b[index_b])
            index_a +=1
            index_b +=1
        else:
            index_a+=1
        
    if(index_b < len(lst_b)):
        lst_a.extend(lst_b)
    
    return lst_a

print(mergeLists([1,4,7,8],[2,3,5,6]))