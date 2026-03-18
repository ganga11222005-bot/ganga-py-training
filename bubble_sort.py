def bubble_sort(array):
    size = len(array)
    for i in range (size):
        swapped = False
        for j in range (0, size-i-1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
                swapped = True
                print(f'Modified array: {array}')
        if not swapped:
            break

    return array

N = int(input("Enter the elements:"))
array = []
for i in range(N):
    num = int(input(f'Enter element {i+1}:'))
    array.append(num)
 
sorted_array = bubble_sort(array)
print("Sorted array:",sorted_array)
