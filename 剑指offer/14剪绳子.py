class Solution:
    def cuttingRope(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]  # dp[0] dp[1]其实没用
        # dp[2] = 1  # 初始化
        for i in range(2, n + 1):
            for j in range(i):
                dp[i] = max(dp[i], max(j * (i - j), dp[j] * (i - j)))
        print(dp)
        return dp[n]


if __name__ == "__main__":
    sol = Solution()
    print(sol.cuttingRope(10))

