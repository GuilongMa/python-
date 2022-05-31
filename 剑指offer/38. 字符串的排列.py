class Solution:
    def permutation(self, s: str) -> [str]:
        if not s:
            return []

        def perm(s):
            if len(s) == 1:
                return [s]
            per = []
            mark_dict = {}
            for i in range(len(s)):
                if not mark_dict.get(s[i]):
                    mark_dict[s[i]] = True
                    left_s = s[:i] + s[i+1:]
                    for j in perm(left_s):
                        per.append(s[i] + j)
            return per
        return perm(s)


class Solution_2:
    def permutation(self, s: str) -> [str]:

        res = []
        c = list(s)
        def perm(x):
            if x == len(c) - 1:
                res.append(''.join(c))
            mark_dict = {}
            for i in range(x, len(c)):
                if not mark_dict.get(c[i]):
                    mark_dict[c[i]] = True
                    c[x], c[i] = c[i], c[x]
                    perm(x+1)
                    c[x], c[i] = c[i], c[x]
        perm(0)
        return res