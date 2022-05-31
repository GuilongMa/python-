def generateGS(pattern_str, l, suffix, prefix):
    for i in range(l):
        j = i
        # 公共后缀子串长度
        k = 0
        while j >= 0 and pattern_str[j] == pattern_str[l - 1 - k]:
            j -= 1
            k += 1
            suffix[k] = j + 1

        if j == -1:
            prefix[k] = True
    print(suffix, prefix)


if __name__ == "__main__":
    pattern_str = "cabcab"
    l = len(pattern_str)
    suffix = [-1] * l
    prefix = [False] * l
    generateGS(pattern_str, l, suffix, prefix)
