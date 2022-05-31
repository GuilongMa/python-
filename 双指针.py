def three_sum_equal_zero(num_list):
    num_list.sort()
    length = len(num_list)
    count = 0
    for i in range(length-2):
        start = i + 1
        end = length - 1
        target = -num_list[i]
        while start < end:
            if target == num_list[start] + num_list[end]:
                count += 1
                start += 1
                end -= 1
            elif target < num_list[start] + num_list[end]:
                end -= 1
            else:
                start += 1
    return count


if __name__ == "__main__":
    num_list = [1, 3, -4, 0, 2, -2, -1]
    print(three_sum_equal_zero(num_list))

