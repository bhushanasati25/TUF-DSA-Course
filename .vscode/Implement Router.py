import collections
import bisect

class Router(object):

    def __init__(self, memoryLimit):
        """
        :type memoryLimit: int
        """
        self.memoryLimit = memoryLimit
        self.q = collections.deque()                
        self.seen = set()                           
        self.dest_ts = collections.defaultdict(list)  
        self.processed = collections.Counter()      

    def addPacket(self, source, destination, timestamp):
        """
        :type source: int
        :type destination: int
        :type timestamp: int
        :rtype: bool
        """
        packet = (source, destination, timestamp)
        if packet in self.seen:
            return False
        if len(self.q) == self.memoryLimit:
            self.forwardPacket()  # evict oldest if full
        self.q.append(packet)
        self.seen.add(packet)
        # timestamps are non-decreasing across all adds, so just append
        self.dest_ts[destination].append(timestamp)
        return True

    def forwardPacket(self):
        """
        :rtype: List[int]
        """
        if not self.q:
            return []
        s, d, t = self.q.popleft()
        self.seen.remove((s, d, t))
        # mark one packet for this destination as processed
        self.processed[d] += 1
        return [s, d, t]

    def getCount(self, destination, startTime, endTime):
        """
        :type destination: int
        :type startTime: int
        :type endTime: int
        :rtype: int
        """
        ts = self.dest_ts.get(destination)
        if not ts:
            return 0
        start_idx = self.processed.get(destination, 0)  # ignore already-forwarded ones
        lo = bisect.bisect_left(ts, startTime, start_idx)
        hi = bisect.bisect_right(ts, endTime, start_idx)
        return hi - lo
