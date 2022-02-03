# Linear search

# def search(arr,x):
#     for i in range(len(arr)):
#         if arr[i]==x:
#             return i
#     return -1

# arr=[1, 4, 6, 7, 45, 655, 56, 78, 90, 54, 23, 54, 12, 21, 67, 
#        0, 98, 91, 29, 19, 32, 65, 20, 34,76 , 87, 99, 43 , 80 ]

# x = 6
# print("element found at index "+str(search(arr,x)))


def linearSearch (array, n , key):
    counter=0
    print("element found at index")
    for i in range(0,n):
        if (array[i]==key):
            counter = counter+1
            print(i+1)

    print("frequency of element is",counter)
    if counter ==0:
        return -1
    else:
        return 1
         

array=[1, 4, 6, 7, 45, 655, 56, 78, 90, 56, 23, 54, 12, 21, 67, 6,
        0, 98, 91, 20, 19, 32, 655, 20, 34,76 , 87, 99, 43 , 80 ]
key=int(input("enter the value you wanna search -")) 
print(key)
n = len(array)
result = linearSearch(array, n , key)
if (result == -1):
    print("\n element not found")

