import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.big_heap = []
        self.small_heap = []

    def addNum(self, num: int) -> None:
        if not self.big_heap:
            heapq.heappush(self.big_heap, -num)
            return
        if num <= -self.big_heap[0]:
            heapq.heappush(self.big_heap, -num)
        else:
            heapq.heappush(self.small_heap, num)
        if len(self.big_heap) - len(self.small_heap) > 1:
            new_num = -heapq.heappop(self.big_heap)
            heapq.heappush(self.small_heap, new_num)
        if len(self.big_heap) - len(self.small_heap) == -1:
            new_num = -heapq.heappop(self.small_heap)
            heapq.heappush(self.big_heap, new_num)


    def findMedian(self) -> float:
        if len(self.big_heap) == len(self.small_heap):
            return (-self.big_heap[0] + self.small_heap[0]) / 2
        else:
            return -self.big_heap[0]


if __name__ == "__main__":
    obj = MedianFinder()
    obj.addNum(1)
    obj.addNum(2)
    obj.addNum(3)
    # obj.addNum(-4)
    # obj.addNum(-2)
    param_2 = obj.findMedian()
    print(param_2)
