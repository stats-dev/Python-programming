


coins = [1,2,5]
amount = 11

dp = [pow(10,4)+1] * (amount + 1)

## DP table
dp[0] = 0
for i in range(len(coins)):
    for j in range(coins[i], amount + 1):
        if dp[j - coins[i]] != pow(10,4)+1:
            dp[j] = min(dp[j], dp[j - coins[i]] + 1)

## 계산 결과
if dp[amount] == pow(10,4)+1:
    print(-1)
else:
    print(dp[amount])

## 노선생님 작업
# memoization
""" 
dp(12)=> min(dp(7) dp(10) dp(11)) +1
dp(7) => min(1, 1, 2) + 1
dp(2) => min(0, 1) + 1
dp(0) => 0
dp(1) => min(0) + 1
memo= {1: 1, 2: 1, 5: 1, }

dp(11) => dp(10), dp(9), dp(6)

dp(10) => 

dp()
 """
class Solution(object):
    def coinChange(self, coins, amount):
        memo = {}
        def dp(amount):
            if amount == 0:
                return 0

            retList = []
            for _, coin in enumerate(coins):
                if amount-coin >= 0: 
                    if amount-coin not in memo:
                        memo[amount-coin] = dp(amount-coin)
                    if memo[amount-coin] != -1:
                        retList.append(memo[amount-coin])

            if retList:
                return min(retList)+1
            else:
                return -1
                
        return dp(amount)


# tabulation
class Solution(object):
    def coinChange(self, coins, amount):
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1 

s = Solution()
print(s.coinChange(coins = [1,2,5], amount = 11))