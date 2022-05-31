import math
from queue import Queue


class TreeNode:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None


# 无重复数据
class TwoFindTree(object):
    def __init__(self, root_val):
        self.root = TreeNode(root_val)

    def insert(self, val):
        cur = self.root
        if not cur:
            self.root = TreeNode(val)
            return
        while cur:
            if val < cur.val:
                if not cur.left:
                    cur.left = TreeNode(val)
                    return
                cur = cur.left
            else:
                if not cur.right:
                    cur.right = TreeNode(val)
                    return
                cur = cur.right

    def insert_recur(self, val, root):
        if root.val == val:
            return
        elif root.val < val:
            if not root.right:
                root.right = TreeNode(val)
                return
            self.insert_recur(val, root.right)
        else:
            if not root.left:
                root.left = TreeNode(val)
                return
            self.insert_recur(val, root.left)

    def delete(self, val):
        """分三种情况
        ①删除的节点没有子节点
        ②删除的节点只有一个节点
        ③删除的节点有两个节点
        """
        cur = self.root
        parent_node = None
        while cur and cur.val != val:
            parent_node = cur
            if val > cur.val:
                cur = cur.right
            else:
                cur = cur.left
        if not cur:
            return

        # ③将删除两个节点的情况转化为①②情况
        if cur.left and cur.right:
            min_cur = cur.right
            parent_min_cur = cur
            while min_cur.left:
                parent_min_cur = min_cur
                min_cur = min_cur.left
            cur.val = min_cur.val
            cur = min_cur
            parent_node = parent_min_cur

        # ①②
        # child是cur的子节点
        if cur.left:
            child = cur.left
        elif cur.right:
            child = cur.right
        else:
            child = None
        # 删除根节点
        if not parent_node:
            self.root = child
        elif parent_node.left == cur:
            parent_node.left = child
        else:
            parent_node.right = child

    def find(self, val):
        cur = self.root
        if not cur:
            return
        while cur:
            if val == cur.val:
                return cur
            elif val < cur.val:
                cur = cur.left
            else:
                cur = cur.right

    def find_max(self):
        cur = self.root
        if not cur:
            return
        while cur.right:
            cur = cur.right
        return cur

    def find_min(self):
        cur = self.root
        if not cur:
            return
        while cur.left:
            cur = cur.left
        return cur

    def in_order(self):
        if not self.root:
            return []
        return self._in_order(self.root)

    def _in_order(self, node):
        if not node:
            return []
        ret = []
        ret.extend(self._in_order(node.left))
        ret.append(node.val)
        ret.extend(self._in_order(node.right))
        return ret

    def _bfs(self):
        """
        bfs
        通过父子关系记录节点编号
        :return:
        """
        if not self.root:
            return []

        ret = []
        q = Queue()
        # 队列[节点，编号]
        q.put((self.root, 1))

        while not q.empty():
            n = q.get()
            if n[0]:
                ret.append((n[0].val, n[1]))
                q.put((n[0].left, n[1] * 2))
                q.put((n[0].right, n[1] * 2 + 1))

        return ret

    def _draw_tree(self):
        """
        可视化
        :return:
        """
        nodes = self._bfs()

        if not nodes:
            print('This tree has no nodes.')
            return

        layer_num = int(math.log(nodes[-1][1], 2)) + 1

        prt_nums = []

        for i in range(layer_num):
            prt_nums.append([None] * 2 ** i)

        for v, p in nodes:
            row = int(math.log(p, 2))
            col = p % 2 ** row
            prt_nums[row][col] = v

        prt_str = ''
        for l in prt_nums:
            prt_str += str(l)[1:-1] + '\n'

        return prt_str

    def __repr__(self):
        # print(str(self.in_order()))
        return self._draw_tree()


if __name__ == "__main__":
    l1 = [4, 2, 5, 6, 1, 7, 3]
    bst = TwoFindTree(l1[0])
    for i in l1[1:]:
        bst.insert(i)

    print(bst)

    # 插入
    bst.insert(1)
    bst.insert(4)
    print(bst)

    # 搜索
    n = bst.find(2)
    print(n.val)

    # # 删除
    # bst.insert(6)
    # bst.insert(7)
    # print(bst)
    # bst.delete(7)
    # print(bst)
    # bst.delete(6)
    # print(bst)
    # bst.delete(4)
    # print(bst)
    #
    # # min max
    # print(bst.find_max())
    # print(bst.find_min())





