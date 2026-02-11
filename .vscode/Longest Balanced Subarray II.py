class SegmentTree:
    def __init__(self, size):
        self.n = size
        self.tree_min = [0] * (4 * size)
        self.tree_max = [0] * (4 * size)
        self.lazy = [0] * (4 * size)

    def _push(self, node):
        """Push lazy values down to children."""
        if self.lazy[node] != 0:
            mid = self.lazy[node]
            
            self.lazy[2 * node] += mid
            self.tree_min[2 * node] += mid
            self.tree_max[2 * node] += mid
            
            self.lazy[2 * node + 1] += mid
            self.tree_min[2 * node + 1] += mid
            self.tree_max[2 * node + 1] += mid
            
            self.lazy[node] = 0

    def update(self, node, start, end, l, r, val):
        if l > end or r < start:
            return
        
        if l <= start and end <= r:
            self.tree_min[node] += val
            self.tree_max[node] += val
            self.lazy[node] += val
            return

        self._push(node)
        mid = (start + end) // 2
        self.update(2 * node, start, mid, l, r, val)
        self.update(2 * node + 1, mid + 1, end, l, r, val)
        
        self.tree_min[node] = min(self.tree_min[2 * node], self.tree_min[2 * node + 1])
        self.tree_max[node] = max(self.tree_max[2 * node], self.tree_max[2 * node + 1])

    def find_first_zero(self, node, start, end):
        if self.tree_min[node] > 0 or self.tree_max[node] < 0:
            return -1
        
        if start == end:
            return start if self.tree_min[node] == 0 else -1
        
        self._push(node)
        mid = (start + end) // 2
        
        res = self.find_first_zero(2 * node, start, mid)
        if res != -1:
            return res
        
        return self.find_first_zero(2 * node + 1, mid + 1, end)

class Solution(object):
    def longestBalanced(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
            
        st = SegmentTree(n)
        last_pos = {}
        max_len = 0
        
        for right in range(n):
            num = nums[right]
            
            val = 1 if num % 2 == 0 else -1
            
            prev_index = last_pos.get(num, -1)
            l = prev_index + 1
            r = right
            
            st.update(1, 0, n - 1, l, r, val)
            last_pos[num] = right
            
            left_index = st.find_first_zero(1, 0, n - 1)
            
            if left_index != -1 and left_index <= right:
                current_len = right - left_index + 1
                if current_len > max_len:
                    max_len = current_len
                    
        return max_len