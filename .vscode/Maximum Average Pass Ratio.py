import heapq

class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        """
        :type classes: List[List[int]]
        :type extraStudents: int
        :rtype: float
        """
        def gain(p, t):
            # Marginal improvement if we add one pass to this class
            return (p + 1.0) / (t + 1.0) - (p * 1.0) / t

        # Max-heap via negative keys: ( -gain, p, t )
        heap = [(-gain(p, t), p, t) for p, t in classes]
        heapq.heapify(heap)

        for _ in range(extraStudents):
            g, p, t = heapq.heappop(heap)
            p += 1
            t += 1
            heapq.heappush(heap, (-gain(p, t), p, t))

        total = 0.0
        for _, p, t in heap:
            total += (p * 1.0) / t
        return total / len(heap)
