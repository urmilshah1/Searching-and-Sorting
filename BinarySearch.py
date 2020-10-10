def BinarySearch(array, low, high, x):
    if high >= low:
        mid = (low+high)//2
    
        if array[mid] ==x:
            return mid
    
        elif array[mid] > x:
            return BinarySearch(array, low, mid-1, x)
    
        else:
            return BinarySearch(array, mid+1, high, x)
    
    else:
        return -1 



array = [2, 3, 4,10, 50]
x = 10

result = BinarySearch(array, 0, len(array)-1, x)

if result != -1:
    print("Element is present at Index", str(result))
else:
    print("Element is not present in array")