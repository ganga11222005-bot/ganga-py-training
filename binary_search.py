<<<<<<< HEAD
# binary search

def binary_search(array, key):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        
        if array[mid] == key:
            return mid
        elif array[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Ueser input
n = int(input("Enter the number of elements:"))
print("*** Enter the element in sorted order ***")
array = []

for i in range(n):
    array.append(int(input()))

key = int(input("Enter the key to be searched:"))
result = binary_search(array, key)

if result != -1:
    print("Element found at the index:",result)
else:
=======
# binary search

def binary_search(array, key):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        
        if array[mid] == key:
            return mid
        elif array[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Ueser input
n = int(input("Enter the number of elements:"))
print("*** Enter the element in sorted order ***")
array = []

for i in range(n):
    array.append(int(input()))

key = int(input("Enter the key to be searched:"))
result = binary_search(array, key)

if result != -1:
    print("Element found at the index:",result)
else:
>>>>>>> 4343a3fb3895dfc01afd1d08d3ddc2b57a997ba3
    print("Element not found")