def min_coins(coins, target_amount):
    #Create a DP array to store the minimum number of coins for each amount
    dp = [float('inf')] * (target_amount + 1)
    
    #Base case: no coins needed to make amount 0
    dp[0] = 0
    
    #Loop through each coin denomination
    for coin in coins:
        # Update the dp array for all amounts from coin to target_amount
        for amount in range(coin, target_amount + 1):
            # If it's possible to make the amount (i.e., amount - coin is valid)
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    
    #If dp[target_amount] is still infinity, it's impossible to make that amount
    if dp[target_amount] == float('inf'):
        return -1
    else:
        return dp[target_amount]

#Example usage
coins = [1, 4, 6, 9, 14]
target_amount = 26

result = min_coins(coins, target_amount)
print(f"Minimum number of coins required: {result}")