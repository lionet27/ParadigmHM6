 
def binary_search(arr:list, num)->int:
    low = 0
    high = len(arr) - 1
    while (low <= high):
        mid = (low + high) // 2
        if arr[mid] < num:
            low = mid + 1
        elif arr[mid] > num:
            high = mid - 1
        else:
            return mid
    return False

arr = [2, 3, 4, 10, 40,67]
x = 20

result = binary_search(arr, x)
print(result)
 










