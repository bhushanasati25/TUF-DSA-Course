class Solution(object):
    def maxDistance(self, side, points, k):
        """
        :type side: int
        :type points: List[List[int]]
        :type k: int
        :rtype: int
        """
        def map_to_1d(x, y):
            if y == 0:
                return x
            elif x == side:
                return side + y
            elif y == side:
                return 3 * side - x
            else:
                return 4 * side - y
                
        A = [map_to_1d(x, y) for x, y in points]
        A.sort()
        N = len(A)
        
        A_ext = A + [a + 4 * side for a in A]
        max_bits = k.bit_length()
        
        def check(D):
            nxt = [2 * N] * (2 * N + 1)
            j = 0
            for i in range(2 * N):
                while j < 2 * N and A_ext[j] - A_ext[i] < D:
                    j += 1
                nxt[i] = j
                
            up = [[2 * N] * max_bits for _ in range(2 * N + 1)]
            for i in range(2 * N + 1):
                up[i][0] = nxt[i]
                
            for bit in range(1, max_bits):
                for i in range(2 * N + 1):
                    if up[i][bit - 1] < 2 * N:
                        up[i][bit] = up[up[i][bit - 1]][bit - 1]
                    else:
                        up[i][bit] = 2 * N
                        
            for i in range(N):
                curr = i
                jumps = k
                
                for bit in range(max_bits):
                    if (jumps >> bit) & 1:
                        curr = up[curr][bit]
                        if curr >= 2 * N:
                            break
                            
                if curr <= i + N:
                    return True
                    
            return False

        low = 1
        high = (4 * side) // k
        ans = 1
        
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return ans