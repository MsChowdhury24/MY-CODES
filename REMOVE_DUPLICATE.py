# def remove_dup(mylist):
#     n=len(mylist)
#     start=0
#     for i in range(1,n):
#         if mylist[i]!=mylist[start]:
#             start+=1 
#             mylist[start]=mylist[i]
#     return start+1 
# mylist=[0,0,1,1,1,2,2,3,3,4]  
# result=remove_dup(mylist) 
# print(result,end=" and ")
# print(mylist[:result])

# COMPLETE PROGRAM - NOT JUST A FUNCTION!

# Step 1: Take input
n = int(input())  # First input: size of array
nums = list(map(int, input().split()))  # Second input: the array

# Step 2: Process (your duplicate removal logic)
def remove_dup_inplace(arr):
    if not arr:
        return 0
    start = 0
    for i in range(1, len(arr)):
        if arr[i] != arr[start]:
            start += 1
            arr[start] = arr[i]
    return start + 1

# Step 3: Call the function
k = remove_dup_inplace(nums)

# Step 4: PRINT THE OUTPUT (MANDATORY!)
print(k)  # Print the length
print(*nums[:k])  # Print the unique elements