class Solution:

    def verifyPostorder(self, postorder: [int]) -> bool:
        last = len(postorder) - 1
        return self.verify(postorder, 0, last)

    def verify(self, postorder, start, last):
        if last - start <= 1:
            return True
        i = start
        root_val = postorder[last]
        while i < last and postorder[i] < root_val:
            i += 1
        for j in range(i, last):
            if postorder[j] < root_val:
                return False
        return self.verify(postorder, start, i-1) and self.verify(postorder, i, last-1)


