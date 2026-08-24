
def Sec_largest_smallest(arr):
    arr.sort()
    smallest=arr[1]
    largest=arr[-2]
    print("smallest",smallest)
    print("largest",largest)
arr = [1, 2, 4, 6, 7, 5]
Sec_largest_smallest(arr)