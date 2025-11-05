import heapq

class Solution(object):
    def findXSum(self, nums, k, x):
        """
        :type nums: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        n = len(nums)
        if k > n:
            return []
        if x == 0:
            return [0] * (n - k + 1)

        cnt = {}
        big, small = [], []  # heaps
        loc = {}             # val -> 1 if in big else 0
        cur_sum = [0]        # mutable container
        big_size = [0]

        # --- cleanup helpers ---
        def clean_big_top():
            while big:
                f, v, val = big[0]
                if cnt.get(val, 0) == f and loc.get(val, 0) == 1:
                    return True
                heapq.heappop(big)
            return False

        def clean_small_top():
            while small:
                nf, nv, val = small[0]
                f, v = -nf, -nv
                if cnt.get(val, 0) == f and loc.get(val, 0) == 0:
                    return True
                heapq.heappop(small)
            return False

        def promote_best():
            if not clean_small_top():
                return False
            nf, nv, val = heapq.heappop(small)
            f, v = -nf, -nv
            if cnt.get(val, 0) != f or loc.get(val, 0) != 0:
                return False
            loc[val] = 1
            cur_sum[0] += v * f
            big_size[0] += 1
            heapq.heappush(big, (f, v, val))
            return True

        def demote_worst():
            if not clean_big_top():
                return False
            f, v, val = heapq.heappop(big)
            if cnt.get(val, 0) != f or loc.get(val, 0) != 1:
                return False
            loc[val] = 0
            cur_sum[0] -= v * f
            big_size[0] -= 1
            heapq.heappush(small, (-f, -v, val))
            return True

        def rebalance():
            target = min(x, len(cnt))
            while big_size[0] < target:
                if not promote_best():
                    break

            while True:
                if not clean_small_top() or not clean_big_top():
                    break
                nf, nv, sval = small[0]
                sf, sv = -nf, -nv
                bf, bv, bval = big[0]
                if (sf > bf) or (sf == bf and sv > bv):
                    demote_worst()
                    promote_best()
                else:
                    break

            target = min(x, len(cnt))
            while big_size[0] > target:
                if not demote_worst():
                    break

        def add_value(val):
            f_old = cnt.get(val, 0)
            if loc.get(val, 0) == 1 and f_old > 0:
                loc[val] = 0
                cur_sum[0] -= val * f_old
                big_size[0] -= 1

            f_new = f_old + 1
            cnt[val] = f_new
            loc.setdefault(val, 0)
            heapq.heappush(small, (-f_new, -val, val))
            rebalance()

        def remove_value(val):
            f_old = cnt.get(val, 0)
            if f_old == 0:
                return
            if loc.get(val, 0) == 1:
                loc[val] = 0
                cur_sum[0] -= val * f_old
                big_size[0] -= 1

            f_new = f_old - 1
            if f_new == 0:
                cnt.pop(val, None)
                loc.pop(val, None)
            else:
                cnt[val] = f_new
                loc[val] = 0
                heapq.heappush(small, (-f_new, -val, val))
            rebalance()

        # initial window
        for i in range(k):
            add_value(nums[i])

        ans = [cur_sum[0]]
        for i in range(k, n):
            remove_value(nums[i - k])
            add_value(nums[i])
            ans.append(cur_sum[0])
        return ans
