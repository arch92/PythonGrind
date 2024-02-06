# Given a list of size n, can you find the second maximum element in the list? 
# Implement your solution in Python and see if your output matches the correct output.

def find_second_maximum(lst):
    # Write your code here
    
    lst.remove(find_max(lst))
    
    return find_max(lst)

def find_max(lst):
    max = lst[0]
    for i in lst:
        if i > max :
            max = i
    return max

print(find_second_maximum([9, 2, 3, 6]))
