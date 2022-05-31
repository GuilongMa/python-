class Solution:
    def cuttingRope(self, n: int) -> int:
        dp = []
        for i in range(n+1):
            dp.append(0)
        for i in range(2, n+1):
            for j in range(i):
                dp[i] = max(dp[i], max(dp[j] * (i-j), j * (i-j)))
        print(dp)
        return dp[n] % 1000000007


if __name__ == "__main__":
    sol = Solution()
    print(sol.cuttingRope(10))