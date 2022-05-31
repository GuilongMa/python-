class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        from queue import Queue
        q = Queue()
        q.put((0, 0))
        s = set()
        s.add((0, 0))
        while not q.empty():
            r, c = q.get()
            if 0 <= r - 1 and (r - 1, c) not in s and self.sum_is_good(r - 1, c, k):
                s.add((r - 1, c))
                q.put((r - 1, c))
            if 0 <= c - 1 and (r, c - 1) not in s and self.sum_is_good(r, c - 1, k):
                s.add((r, c - 1))
                q.put((r, c - 1))
            if r + 1 < m and (r + 1, c) not in s and self.sum_is_good(r + 1, c, k):
                s.add((r + 1, c))
                q.put((r + 1, c))
            if c + 1 < n and (r, c + 1) not in s and self.sum_is_good(r, c + 1, k):
                s.add((r, c + 1))
                q.put((r, c + 1))
        return len(s)

    def sum_is_good(self, r, c, k):
        def num_sum(n):
            ans = 0
            while n:
                ans += n % 10
                n //= 10
            return ans

        return num_sum(r) + num_sum(c) <= k


# def digitsum(n):
#     ans = 0
#     while n:
#         ans += n % 10
#         n //= 10
#     return ans
#
# class Solution_2:
#     def movingCount(self, m: int, n: int, k: int) -> int:
#         from queue import Queue
#         q = Queue()
#         q.put((0, 0))
#         s = set()
#         while not q.empty():
#             x, y = q.get()
#             if (x, y) not in s and 0 <= x < m and 0 <= y < n and digitsum(x) + digitsum(y) <= k:
#                 s.add((x, y))
#                 for nx, ny in [(x + 1, y), (x, y + 1)]:
#                     q.put((nx, ny))
#         return len(s)
