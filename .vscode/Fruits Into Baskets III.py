class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (4 * self.n)
        self.build(nums, 0, 0, self.n - 1)

    def build(self, nums, node, l, r):
        if l == r:
            self.tree[node] = nums[l]
        else:
            mid = (l + r) // 2
            self.build(nums, 2 * node + 1, l, mid)
            self.build(nums, 2 * node + 2, mid + 1, r)
            self.tree[node] = max(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def query(self, node, l, r, target):
        # If no basket can satisfy the condition
        if self.tree[node] < target:
            return -1
        if l == r:
            return l
        mid = (l + r) // 2
        left_result = self.query(2 * node + 1, l, mid, target)
        if left_result != -1:
            return left_result
        return self.query(2 * node + 2, mid + 1, r, target)

    def update(self, node, l, r, idx):
        if l == r:
            self.tree[node] = 0
        else:
            mid = (l + r) // 2
            if idx <= mid:
                self.update(2 * node + 1, l, mid, idx)
            else:
                self.update(2 * node + 2, mid + 1, r, idx)
            self.tree[node] = max(self.tree[2 * node + 1], self.tree[2 * node + 2])


class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """
        n = len(baskets)
        tree = SegmentTree(baskets)
        unplaced = 0

        for fruit in fruits:
            idx = tree.query(0, 0, n - 1, fruit)
            if idx == -1:
                unplaced += 1
            else:
                tree.update(0, 0, n - 1, idx)

        return unplaced
