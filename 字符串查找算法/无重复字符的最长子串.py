def length_of_longest_sub_string(s: str) -> int:
    l = 0
    for i in range(len(s)):
        count = 0
        hash_map = {}
        for j in s[i:]:
            if j in hash_map:
                break
            else:
                hash_map[j] = True
                count += 1
                l = max(l, count)
    return l


def length_of_longest_sub_string2(s: str) -> int:
    # 哈希集合，记录每个字符是否出现过
    occ = set()
    n = len(s)
    # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
    rk, ans = -1, 0
    for i in range(n):
        if i != 0:
            # 左指针向右移动一格，移除一个字符
            occ.remove(s[i - 1])
        while rk + 1 < n and s[rk + 1] not in occ:
            # 不断地移动右指针
            occ.add(s[rk + 1])
            rk += 1
        # 第 i 到 rk 个字符是一个极长的无重复字符子串
        ans = max(ans, rk - i + 1)
    return ans


if __name__ == "__main__":
    s = ' '
    print(length_of_longest_sub_string(s))
