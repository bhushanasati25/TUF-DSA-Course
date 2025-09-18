import heapq

class TaskManager(object):

    def __init__(self, tasks):
        """
        :type tasks: List[List[int]]  # [userId, taskId, priority]
        """
        # taskId -> (userId, priority)
        self.info = {}
        # max-heap (via negatives): entries are (-priority, -taskId, taskId)
        self.heap = []
        for u, t, p in tasks:
            self.add(u, t, p)

    def add(self, userId, taskId, priority):
        """
        :type userId: int
        :type taskId: int
        :type priority: int
        :rtype: None
        """
        # If taskId already exists, treat as update (LeetCode won't pass dup IDs, but safe)
        self.info[taskId] = (userId, priority)
        heapq.heappush(self.heap, (-priority, -taskId, taskId))

    def edit(self, taskId, newPriority):
        """
        :type taskId: int
        :type newPriority: int
        :rtype: None
        """
        if taskId not in self.info:
            return
        userId, _ = self.info[taskId]
        self.info[taskId] = (userId, newPriority)
        heapq.heappush(self.heap, (-newPriority, -taskId, taskId))

    def rmv(self, taskId):
        """
        :type taskId: int
        :rtype: None
        """
        # Lazy delete: just drop from map
        if taskId in self.info:
            del self.info[taskId]

    def execTop(self):
        """
        :rtype: int
        """
        # Pop stale entries until we find a valid, up-to-date one
        while self.heap:
            neg_p, neg_tid, tid = heapq.heappop(self.heap)
            if tid in self.info:
                userId, priority = self.info[tid]
                # Validate it's the latest version (matches priority)
                if -neg_p == priority:
                    # Consume it
                    del self.info[tid]
                    return userId
                # else: stale priority -> keep popping
        return -1



# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()