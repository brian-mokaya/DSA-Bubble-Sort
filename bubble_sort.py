array = [800, 543, 123, 456, 789, 234, 567, 890, 345, 678, 901]
print("Original array is:", array)

# Bubble Sort Algorithm Implementation

n = len(array)

for i in range(n-1):
    for j in range(n-i-1):
        if array[j] > array[j+1]:
            # Swap if the element found is greater
            # array[j], array[j+1] = array[j+1], array[j] 
            temp = array[j]
            array[j] = array[j+1]
            array[j+1] = temp


print("Sorted array is:", array)
        