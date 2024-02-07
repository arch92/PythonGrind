# Implement a function called max_min(lst) which will re-arrange the elements of a sorted list of positive integers, 
# such that the 0th index will have the largest number, the 1st index will have the smallest, 
# and the 2nd index will have second-largest, and so on. In other words, all the even-numbered indices will have the largest numbers in the list in descending order 
# and the odd-numbered indices will have the smallest numbers in ascending order.

def max_min(lst):

    # The code starts by initializing variables for the first and last indices of the list.
    # It then creates a result list with the same length as the input list.
    # The code uses a while loop to iterate through the list and pop elements from the input list to fill the result list at even indices.
    # After that, it checks if the last index is even or odd and sets the index variable accordingly.
    # Another while loop is used to fill the result list at odd indices by popping elements from the input list.
    # Finally, the result list is returned.
    first = 0
    last = len(lst) - 1
    result = list(range(len(lst)))
    index = 0
    while(index <= last) :
        result[index] = lst.pop()
        index+=2
    # checks for odd or even indices
    if last%2==0:
        index=last - 1
    else:
        index=last
        
    while(index >= 1) :
        result[index] = lst.pop()
        index-=2
        
    return result

print(max_min([2,4,6,8,10]))
