from typing import List

def maxProfit(prices: List[int]) -> int:
    # [7,1,5,3,6,4]
    # whenever you see an increase from one element to the next, it is worth to trade
    # let's loop over the array and compare the current element with the next
    # c = 7, n = 1 => profit = 0
    # c = 1, n = 5 => profit = 4
    # c = 5, n = 3 => profit = 0
    # c = 3, n = 6 => profit = 3
    # c = 6, n = 4 => profit = 0

    total_profit = 0
    for i in range(len(prices) - 1):
        profit = prices[i + 1] - prices[i]
        if profit > 0:
            total_profit += profit
    return total_profit
    
    

if __name__ == '__main__':
    print(maxProfit([7,1,5,3,6,4]))
    print(maxProfit([1,2,3,4,5]))
    print(maxProfit([7,6,4,3,1]))