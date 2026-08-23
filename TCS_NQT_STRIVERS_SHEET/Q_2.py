# Find the largest no. in an array

def Largest_number(arr):
    largest=arr[0]
    for num in arr:
        if num>largest:
            largest=num
    print(largest)
arr=[1,2,3,4,5,6,7]
(Largest_number(arr))
    