class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [[0 for _ in range(amount+1)] for _ in range(len(coins)+1)]
        dp[0][0] = 1
        for i in range(1,len(coins)+1):
            dp[i][0] = 1
        for i in range(1,len(coins)+1):
            for j in range(amount+1):
                if j < coins[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
        return dp[-1][-1] 