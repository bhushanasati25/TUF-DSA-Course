import heapq
from collections import defaultdict

class MovieRentingSystem(object):

    def __init__(self, n, entries):
        """
        :type n: int
        :type entries: List[List[int]]
        """
        self.price = {(s, m): p for s, m, p in entries}

        self.movie_heap = defaultdict(list)
        for s, m, p in entries:
            heapq.heappush(self.movie_heap[m], (p, s))

        self.rented_heap = []

        self.rented = set()

    def search(self, movie):
        """
        :type movie: int
        :rtype: List[int]
        """
        h = self.movie_heap[movie]
        res, temp = [], []

        while h and len(res) < 5:
            p, s = heapq.heappop(h)
            temp.append((p, s))  # keep heap intact
            if (s, movie) not in self.rented:
                res.append(s)

        for item in temp:
            heapq.heappush(h, item)

        return res

    def rent(self, shop, movie):
        """
        :type shop: int
        :type movie: int
        :rtype: None
        """
        self.rented.add((shop, movie))
        heapq.heappush(self.rented_heap, (self.price[(shop, movie)], shop, movie))

    def drop(self, shop, movie):
        """
        :type shop: int
        :type movie: int
        :rtype: None
        """
        self.rented.discard((shop, movie))

    def report(self):
        """
        :rtype: List[List[int]]
        """
        res, keep = [], []
        seen = set()

        while self.rented_heap and (self.rented_heap[0][1], self.rented_heap[0][2]) not in self.rented:
            heapq.heappop(self.rented_heap)

        while self.rented_heap and len(res) < 5:
            p, s, m = heapq.heappop(self.rented_heap)
            if (s, m) in self.rented:
                if (s, m) not in seen:
                    res.append([s, m])
                    seen.add((s, m))
                    keep.append((p, s, m))
    
        for item in keep:
            heapq.heappush(self.rented_heap, item)

        return res
