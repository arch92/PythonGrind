#Basic Operations
sample_list = ['a','apple',4,3.14]
print(sample_list)
# Initializing lists
empty_list= []
range_list = list(range(10))
print(range_list)

a_list = [2, 'Educative', 'A']


def foo():
    print('Hello from foo()!')


another_list = [a_list, 'Python', foo, ['yet another list']]

print(another_list[0])  # Elements of 'aList'
print(another_list[0][1])  # Second element of 'aList'
print(another_list[1])  # 'Python'
print(another_list[3])  # 'yet another list'

# You can also invoke the functions inside a list!
another_list[2]()  # 'Hello from foo()!'

another_list.append(10) #append
print(another_list)

another_list.insert(0,2) #insert
print(another_list)
another_list.remove(2)
print(another_list)
another_list.pop()
print(another_list)
another_list.reverse()
print(another_list)
# Slicing
n = list(range(10))
print(n[3:])  # 3, 4, 5, 6, 7, 8, 9
print(n[:3])  # 0 1 2
print(n[:])  # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

# list = list(range(10))
print(n[0:9:2])  # 0, 2, 4, 6, 8  
print(n[9:0:-2])  # 9, 7, 5, 3, 1

x = list(range(5))
print(x)  # 0, 1, 2, 3, 4
x[1:4] = [45, 21, 83]
print(x)  # 0, 45, 21, 83, 4


print(n)  # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
del n[::2]
print(n)  # 1, 3, 5, 7, 9


print(n)
print(n[4:-1])  # 4, 5, 6, 7, 8

my_string = "somehow"
string1 = my_string[:4]
string2 = my_string[4:]
print(string1, string2)