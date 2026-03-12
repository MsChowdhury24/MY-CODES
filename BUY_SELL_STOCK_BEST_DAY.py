# prices=[7,1,5,3,6,4]
# n=len(prices)
# min_price=prices[0]
# profit=0
# for i in range(1,n):
#     curr_profit=prices[i]-min_price
#     if curr_profit>profit:
#         profit=curr_profit               #TIME COMPLEXITY :- O(n)
#     min_price=min(min_price,prices[i])
#     profit=max(profit,curr_profit)
# print(f"profit is:{profit}")
# print(f"the min_price:{min_price}")


def maximum_profit(prices):
    min_price=prices[0]
    max_profit=0
    for price in prices:
        if price<min_price:
            min_price=price
        if price-min_price>max_profit:
            max_profit=price-min_price
    return max_profit 
if __name__ == "__main__":
    input_str = input().strip()
    prices = list(map(int, input_str[1:-1].split(',')))  #TYPE1 INPUT FORMAT
    #prices = list(map(int, input().split(',')))         #TYPE2 INPUT FORMAT
    #prices = list(map(int, input().split()))            #TYPE3 INPUT FORMAT
    maximum_profit(prices)
result=maximum_profit(prices)
print(result)

