# count the number of swaps during bubble sort
def bubble_sort(array):
    n = len(array)
    swap_count = 0

    for i in range (n):
        swapped = False

        for j in range (0,n-i-1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
                swap_count += 1
                swapped = True
        print(f'After pass{i+1}: {array}')

        if not swapped:
            break

    return array,swap_count

N = int(input("Enter the elements:"))
array = []
for i in range(N):
    num = int(input(f'Enter element {i+1}:'))
    array.append(num)
 
sorted_array,swaps = bubble_sort(array)
print("Sorted array:",sorted_array)
print("Total number of swap:",swaps)
