import heapq


def choushu(num):
    nums = [2, 3, 5]
    heap = []
    heapq.heappush(heap, 1)
    s_dict = {1:True}
    first = None
    while num:
        first = heapq.heappop(heap)
        for i in nums:
            new_num = first * i
            if not s_dict.get(new_num):
                heapq.heappush(heap, new_num)
                s_dict[new_num] = True
        num -= 1
    if first is not None:
        return first


if __name__ == "__main__":
    print(choushu(10))
