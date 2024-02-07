# Implement a function rearrange(lst) which rearranges the elements such that all the negative elements appear on the left and positive elements appear at the right of the list. 
# Note that it is not necessary to maintain the sorted order of the input list.

# The code uses a two-pointer approach to rearrange the list.
# It iterates through the list using two pointers, low_index and next_index.
# If the element at low_index is negative, it increments low_index.
# If the element at next_index is negative, it swaps the elements at low_index and next_index, and increments low_index.
# The code continues this process until next_index reaches the end of the list.
# Finally, it returns the rearranged list.

def rearrange(lst):

    # Replace this placeholder return statement with your code
    low_index = 0
    next_index = 1
    while(low_index<next_index and next_index<len(lst)):
        if lst[low_index] < 0:
            low_index+=1
        if lst[next_index] < 0 :
            temp = lst[low_index]
            lst[low_index] = lst[next_index]
            lst[next_index] = temp
            low_index+=1
        next_index+=1
        
    return lst

print(rearrange([1,-2,3,-4,5]))
