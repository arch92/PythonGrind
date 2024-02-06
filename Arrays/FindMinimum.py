# Given a list of size ‘n,’ 
# can you find the minimum value in the list? Implement your solution in Python and see if your output matches the expected output.

def find_minimum(arr):
    # Write your code here
    min = arr[0]
    for i in range(1,len(arr)):
        if min > arr[i]:
            min = arr[i]
    return min

print(find_minimum([3,6,2,4,1,7]))
