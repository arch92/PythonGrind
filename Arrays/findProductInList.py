# Given a list, modify it so that each index stores the product of all elements in the list except the element at the index itself.

# The algorithm for this solution is to first create a new 
# list with products of all elements to the left of each element as done on lines 4-6. 
# Then multiply each element in that list to the product of all the elements to the right of 
# the list by traversing it in reverse as done on lines 9-11.


def find_product(lst):
    left = 1
    products = []
    for num in lst:
        products.append(left)
        left = left * num
    right = 1
    for n in range(len(lst)-1,-1,-1):
        products[n] = products[n] * right
        right = right * lst[n]
        
    
    return products

print(find_product([1,2,3,4]))
        