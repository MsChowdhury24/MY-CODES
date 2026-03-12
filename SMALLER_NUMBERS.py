import TODO
print(TODO.__doc__)

# METHOD1: HERE WE ARE CONSIDERING "i" indicates the position
#and nums[i] indicates the value of the list at that position.
#i.e. for the list  nums[8,1,2,2,3]   if i=0 then nums[0]=8 and so on. 
def smallerNumbersThanCurrent(nums):
    print("Print i's and nums[i]'s for METHOD1:")
    ans = []
    for i in range(len(nums)):
        print("i=",i,"--> nums[i]=",nums[i])
        total = 0
        for j in range(len(nums)):
            if nums[j] < nums[i]:
                total += 1
        ans.append(total)
    return ans

result = smallerNumbersThanCurrent([8, 1, 2, 2, 3])
print(f"OUTPUT FOR METHOD 1: {result}")

# METHOD2: HERE WE ARE DIRECTLY INDICATING "i" AS THE VALUE OF THE LIST 
#i.e. for nums=[8,1.,2,2,3] , when i=8 , j=1/2/2/3 and start checking the j's
#that are less than i=8 and continue similarly.

def smallerNumbersThanCurrent(nums):
    print()
    print("Print the i's for METHOD2:",*nums)
    ans = []
    for i in nums:
        total = 0
        for j in nums:
            if j < i:
                total += 1
        ans.append(total)
    return ans

result = smallerNumbersThanCurrent([8, 1, 2, 2, 3])
print(f"OUTPUT FOR METHOD 2: {result}")