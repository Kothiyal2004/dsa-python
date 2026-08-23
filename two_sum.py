
# def two_sum(arr,target):
    
#     for i in range(len(arr)):  # time complexity O(n2)
#         for j in range(i+1,(len(arr))):
#             if arr[i]+arr[j]==target:
#                 return [i,j]
# print(two_sum([1,2,3,5],14))



# def two_sum(arr,target):
#     for i in range(len(arr)):
#         if target==arr[i]+arr[i+1]:    # optimal time complexity O(n)
#             return [i,i+1]
# print(two_sum([1,2,3,5],5))


def two_sum(arr,target):
    seen={}
    for i , num in enumerate(arr):
        diff=target-num
        if diff in seen:
            return[seen[diff],i]
        seen[num]=i
print(two_sum([1,2,3,5],4))