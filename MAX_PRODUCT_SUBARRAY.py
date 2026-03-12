nums=[0,3,-1]
n=len(nums)
final_product=float('-inf') 
product_L=1
max_product_L=float('-inf')
for i in range(n):
    print("i=",i,"nums[i]=",nums[i])
    print()
    if nums[i]==0:
        product_L=0
        max_product_L=max(product_L,max_product_L)
        product_L=1
    else:
        product_L*=nums[i]
        max_product_L=max(product_L,max_product_L)

product_R=1
max_product_R=float('-inf')
for j in reversed(range(n)):
    print("j=",j,"nums[j]=",nums[j])
    print()
    if nums[j]==0:
        product_R=0
        max_product_R=max(product_R,max_product_R)
        product_R=1
    else:
        product_R*=nums[j]
        max_product_R=max(product_R,max_product_R)
        
final_product=max(final_product,max(max_product_L,max_product_R))
print(f"Max. Product Subarray is:{final_product}")


#TIME COMPLEXITY IS: O(N)