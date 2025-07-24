array = [800, 543, 123, 456, 789, 234, 567, 890, 345, 678, 901]
print ("Original array is:", array)

# Improved Bubble Sort Algorithm Implementation
n = len(array)
for i in range(n-1):
    swapped = False
    for j in range (n-i-1):
        if array[j] > array[j+1]:

            array[j],array[j+1] = array[j+1], array[j]  # Swap if the element found is greater(this is a more Pythonic, which is the same as using a temporary variable)
            swapped = True
            if not swapped:
                break

print("The Sorted array is:", array)




