# Given a list and a number "k", find two numbers from the list that sum to "k".

def find_sum(lst, k):
    # Write your code here
    lst.sort()
    start = 0
    end = len(lst)-1
    while(start<=end):
        num = k-lst[start]
        print(num)
        if(num>lst[end]):
            start+=1
        if(num==lst[end]):
            return [lst[start],num]
    return []

print(find_sum([2,5,10,4,16],18))
