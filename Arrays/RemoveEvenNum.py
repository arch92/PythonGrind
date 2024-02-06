# Given a list of size n, remove all even integers from it. Implement this solution in Python and see if it runs without an error.

def remove_even(input_list):
    odd_lst = []
    for i in input_list:
        if i%2 != 0:
            odd_lst.append(i)
        
    return odd_lst

def lst_compren(lst):
    return [i for i in lst if i%2!=0]

#TC O(n)
print(remove_even([1,2,3,4,5,6]))
print(lst_compren([34,75,4,53,-23]))
