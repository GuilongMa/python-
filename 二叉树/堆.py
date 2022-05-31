class Heap(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        self.root = [None] * (capacity + 1)

    def _siftup(self):
        i = self.count
        while i // 2 and self.root[i] > self.root[i // 2]:
            self.root[i], self.root[i // 2] = self.root[i // 2], self.root[i]
            i = i // 2

    def insert(self, val):
        if self.count == self.capacity:
            return
        self.count += 1
        self.root[self.count] = val
        self._siftup()

    def delete_top(self):
        if not self.count:
            return
        top_val = self.root[1]
        self.root[1] = self.root[self.count]
        self.count -= 1
        self._siftdown(self.root, self.count, 1)
        return top_val

    @staticmethod
    def _siftdown(nums, count, root_index):
        while True:
            larger_child_index = root_index
            if root_index * 2 <= count and nums[root_index] < nums[root_index * 2]:
                larger_child_index = root_index * 2
            if root_index * 2 + 1 <= count and nums[larger_child_index] < nums[root_index * 2 + 1]:
                larger_child_index = root_index * 2 + 1
            if larger_child_index == root_index:
                break
            nums[root_index], nums[larger_child_index] = nums[larger_child_index], nums[root_index]
            root_index = larger_child_index

    @classmethod
    def build_heap(cls, nums):
        for num_index in range(len(nums)//2, 0, -1):
            cls._siftdown(nums, len(nums) - 1, num_index)

    @classmethod
    def sort(cls, nums):
        cls.build_heap(nums)
        count_index = len(nums) - 1
        while count_index > 1:
            nums[1], nums[count_index] = nums[count_index], nums[1]
            count_index -= 1
            cls._siftdown(nums, count_index, 1)

    def __repr__(self):
        return self.root[1:self.count+1].__repr__()


if __name__ == "__main__":
    hp = Heap(10)
    hp.insert(3)
    hp.insert(9)
    hp.insert(1)
    hp.insert(8)
    hp.insert(7)
    hp.insert(3)
    print(hp)
    for _ in range(6):
        print(hp.delete_top())
    a = [0, 6, 3, 4, 0, 9, 2, 7, 5, -2, 8, 1, 6, 10]
    Heap.sort(a)
    print(a[1:])









