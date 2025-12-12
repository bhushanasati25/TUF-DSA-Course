import heapq

class Solution(object):
    def countMentions(self, numberOfUsers, events):
        """
        :type numberOfUsers: int
        :type events: List[List[str]]
        :rtype: List[int]
        """

        def key_fn(e):
            typ, t, _ = e
            pr = 0 if typ == "OFFLINE" else 1
            return (int(t), pr)
        events.sort(key=key_fn)

        counts = [0] * numberOfUsers
        lazy_all = 0                     
        offline_set = set()              
        restore_heap = []                

        def restore_if_needed(current_time):
            while restore_heap and restore_heap[0][0] <= current_time:
                rt, u = heapq.heappop(restore_heap)
                if u in offline_set:
                    offline_set.remove(u)

        all_users_set = set(range(numberOfUsers))

        for typ, t_str, data in events:
            t = int(t_str)
            restore_if_needed(t)

            if typ == "OFFLINE":
                user = int(data)
                offline_set.add(user)
                heapq.heappush(restore_heap, (t + 60, user))
            else:  
                if data == "ALL":
                    lazy_all += 1
                elif data == "HERE":
                    for u in all_users_set:
                        if u not in offline_set:
                            counts[u] += 1
                else:
                    tokens = data.split()
                    for tok in tokens:
                        if tok.startswith("id"):
                            try:
                                uid = int(tok[2:])
                                if 0 <= uid < numberOfUsers:
                                    counts[uid] += 1
                            except ValueError:
                                continue

        return [counts[i] + lazy_all for i in range(numberOfUsers)]
