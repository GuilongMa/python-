class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_length = 0
        max_str = ''
        for i in range(n):
            left = i
            right = i + 1
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            if right - left -1 > max_length:
                max_length = right - left -1
                max_str = s[left+1:right]
            left = i
            right = i
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            if right - left - 1 > max_length:
                max_length = right - left -1
                max_str = s[left+1:right]

        return max_str


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestPalindrome("abcda"))
