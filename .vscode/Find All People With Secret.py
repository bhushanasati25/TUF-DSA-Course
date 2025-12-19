import collections

class Solution(object):
    def findAllPeople(self, n, meetings, firstPerson):
        """
        :type n: int
        :type meetings: List[List[int]]
        :type firstPerson: int
        :rtype: List[int]
        """
        meetings.sort(key=lambda x: x[2])
        
        known = {0, firstPerson}
        
        i = 0
        while i < len(meetings):
            j = i
            curr_time = meetings[i][2]
            
            while j < len(meetings) and meetings[j][2] == curr_time:
                j += 1
            
            current_batch = meetings[i:j]
        
            graph = collections.defaultdict(list)
            participants = set()
            
            for p1, p2, _ in current_batch:
                graph[p1].append(p2)
                graph[p2].append(p1)
                participants.add(p1)
                participants.add(p2)
            
            queue = collections.deque()
            for p in participants:
                if p in known:
                    queue.append(p)
            
            while queue:
                person = queue.popleft()
                for neighbor in graph[person]:
                    if neighbor not in known:
                        known.add(neighbor)
                        queue.append(neighbor)
            
            i = j
            
        return list(known)