def insertion_sort_ascending(array):
    for index in range(1, len(array)):
        currentValue = array[index]
        currentPosition = index

        while currentPosition > 0 and array[currentPosition - 1] > currentValue:
            array[currentPosition] = array[currentPosition - 1]
            currentPosition = currentPosition - 1

        array[currentPosition] = currentValue

def insertion_sort_descending(array):
    for index in range(1, len(array)):
        currentValue = array[index]
        currentPosition = index

        while currentPosition > 0 and array[currentPosition - 1] < currentValue:
            array[currentPosition] = array[currentPosition - 1]
            currentPosition = currentPosition - 1

        array[currentPosition] = currentValue


array = [ 4, 22, 2, 5, 89, 42, 56, 7, 11, 9, 45]
print("Element before sorting :")
print(array)
insertion_sort_ascending(array)
print("Element after sorting in ascending order : " + str(array))
insertion_sort_descending(array)
print("Element after sorting in descending order : " + str(array))

def BinSearch(array,Key,Low,high):
    if Low>high:
        return -1
    mid = int((Low+high)/2)

    if Key==array[mid]:
        return mid
    elif Key<array[mid]:
        high=mid-1
    else:
        Low=mid+1
        return BinSearch(array,Key,Low,high)

array = [ 4, 22, 2, 5, 89, 42, 56, 7, 11, 9, 45]
item=int(input("Enter search item:"))

print()
result = BinSearch(array,item,0,len(array)-1)

if result>=0:
    print(item,"Found at index",result)
else:
    print("sorry!", item, "Not found in array")

