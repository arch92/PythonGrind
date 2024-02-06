# Given a list, find the first integer which is unique in the list. 
# Unique means the number does not repeat and appears only once in the whole list. 
# Implement your solution in Python and see if it runs correctly

def find_first_unique(lst):
    # Write your code here
    result=[]
    for num in lst:
        if num not in result:
            result.append(num)
        else:
            result.remove(num)
    return result[0]
 print(find_first_unique([9, 2, 3, 2, 6, 6]))
