class Solution(object):
    def maxSubarrays(self, n, conflictingPairs):
        """
        :type n: int
        :type conflictingPairs: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict
        import heapq

        m = len(conflictingPairs)
        
        # Step 1: Normalize conflicts as (L, R), store with conflict ID
        conflict_by_L = defaultdict(list)
        for idx, (a, b) in enumerate(conflictingPairs):
            L, R = min(a, b), max(a, b)
            conflict_by_L[L].append((R, idx))  # R is right bound, idx is conflict ID
        
        # Step 2: Initialize
        dp_first = [n+1] * (n+2)   # dp_first[i] = smallest R such that L >= i
        dp_second = [n+1] * (n+2)  # second smallest R for backup
        id_first = [-1] * (n+2)    # conflict ID responsible for smallest R
        id_second = [-1] * (n+2)   # conflict ID responsible for second smallest R
        gain = [0] * m             # gain[i] = number of extra subarrays unlocked by removing conflict i
        
        # Step 3: Sweep from right to left and build dp arrays
        for i in range(n, 0, -1):
            # carry forward
            dp_first[i] = dp_first[i+1]
            dp_second[i] = dp_second[i+1]
            id_first[i] = id_first[i+1]
            id_second[i] = id_second[i+1]

            # update with current conflicts
            for R, idx in conflict_by_L[i]:
                if R < dp_first[i]:
                    dp_second[i] = dp_first[i]
                    id_second[i] = id_first[i]
                    dp_first[i] = R
                    id_first[i] = idx
                elif R < dp_second[i]:
                    dp_second[i] = R
                    id_second[i] = idx

        # Step 4: Compute base total and potential gains
        total = 0
        for i in range(1, n+1):
            total += dp_first[i] - i
            if id_first[i] != -1:
                gain[id_first[i]] += dp_second[i] - dp_first[i]

        # Step 5: Add best gain
        max_gain = max(gain) if gain else 0
        return total + max_gain
