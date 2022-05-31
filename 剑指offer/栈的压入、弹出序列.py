class Solution:

    def validateStackSequences(self, pushed: [int], popped: [int]) -> bool:
        j = 0
        for i in range(len(popped)):
            while pushed[j] != popped[i]:
                j += 1
                if j == len(pushed):
                    return False
            pushed.pop(j)
            if j != 0:
                j -= 1
        return True


if __name__ == "__main__":
    sol = Solution()
    pushed = [1,2,3,4,5]

    poped = [4,5,3,2,1]
    print(sol.validateStackSequences(pushed, poped))