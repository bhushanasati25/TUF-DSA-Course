class Solution(object):
    def minimumHammingDistance(self, source, target, allowedSwaps):
        """
        :type source: List[int]
        :type target: List[int]
        :type allowedSwaps: List[List[int]]
        :rtype: int
        """
        n = len(source)
        parent = list(range(n))
        
        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]
        
        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j
                
        for u, v in allowedSwaps:
            union(u, v)
            
        components = collections.defaultdict(list)
        for i in range(n):
            components[find(i)].append(i)
            
        hamming_distance = 0
        
        for root, indices in components.items():
            source_count = collections.Counter(source[i] for i in indices)
            
            for i in indices:
                needed_val = target[i]
                if source_count[needed_val] > 0:
                    source_count[needed_val] -= 1
                else:
                    hamming_distance += 1
                    
        return hamming_distance