class Solution:

    def exist(self, board: [[str]], word: str) -> bool:
        if not board:
            return False
        visited = []
        m, n = len(board), len(board[0])
        for i in range(m):
            visited.append([False]*n)
        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0]:
                    cur = r, c
                    visited[r][c] = True
                    word_cur = 1
                    if self.retravel(cur, visited, word_cur, word, board, m, n):
                        return True
                    visited[r][c] = False
        return False

    def retravel(self, cur, visited, word_cur, word, board, m, n):
        if word_cur == len(word):
            return True
        for x in self.get_next(visited, cur, board, word_cur, word, m, n):
            visited[x[0]][x[1]] = True
            if not self.retravel(x, visited, word_cur + 1, word, board, m, n):
                visited[x[0]][x[1]] = False
            else:
                return True

    def get_next(self, visited, cur, board, word_cur, word, m, n):
        tuple_list = []
        r, c = cur
        if 0 <= r - 1:
            if not visited[r - 1][c] and board[r - 1][c] == word[word_cur]:
                tuple_list.append((r - 1, c))
        if 0 <= c - 1:
            if not visited[r][c - 1] and board[r][c - 1] == word[word_cur]:
                tuple_list.append((r, c - 1))
        if r + 1 <= m - 1:
            if not visited[r + 1][c] and board[r + 1][c] == word[word_cur]:
                tuple_list.append((r + 1, c))
        if c + 1 <= n - 1:
            if not visited[r][c + 1] and board[r][c + 1] == word[word_cur]:
                tuple_list.append((r, c + 1))
        return tuple_list


# class Solution:
#     def exist(self, board: List[List[str]], word: str) -> bool:
#         def dfs(i, j, k):
#             if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]: return False
#             if k == len(word) - 1: return True
#             tmp, board[i][j] = board[i][j], '/'
#             res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
#             board[i][j] = tmp
#             return res
#
#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 if dfs(i, j, 0): return True
#         return False

if __name__ == "__main__":
    board = [["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]]
    word = "AAB"
    sol = Solution()
    print(sol.exist(board, word))



