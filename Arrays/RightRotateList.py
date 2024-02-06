# Given a list, can you rotate its elements by one index from right to left? 
# Implement your solution in Python and see if your code runs successfully.
def right_rotate(lst, k):
    if len(lst) == 0:
        k = 0
    else:
        k = k % len(lst)
    return lst[-k:] + lst[:-k]

print(right_rotate([10,20,30,40,50],3))