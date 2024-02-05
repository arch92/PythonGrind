import array

#Initialize arrays
new_array = array.array('i',[1,2,3,4])
print(new_array)

#Slicing
print(new_array[:])
print(new_array[1:2])
print(new_array[:-2])

#Changing elements in arrays
new_array[1] = 20
print(new_array)
new_array[2:] = array.array('i',[5,6])
print(new_array)

new_array.append(10) # concatenate one item
print(new_array)
new_array.extend([2,3,4]) # concatenate more than one item
print(new_array)

extend_array = array.array('i',[2,5,6])
print(new_array + extend_array)

del extend_array[0]
print(extend_array)

del extend_array
new_array.remove(3)
print(new_array)
new_array.pop(0)
print(new_array)



