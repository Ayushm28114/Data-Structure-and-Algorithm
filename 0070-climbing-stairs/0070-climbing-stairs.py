class Solution:
    def climbStairs(self, n: int) -> int:
        ans = self.memo(n,{})
        return ans

    def memo(self, n, dp: dict):
        if n<3:
            return n
        
        if n in dp:
            return dp[n]
        
        dp[n] = self.memo(n-1,dp) + self.memo(n-2,dp)
        return dp[n]