from collections import deque

class Solution(object):
    def maxCandies(self, status, candies, keys, containedBoxes, initialBoxes):
        """
        :type status: List[int]
        :type candies: List[int]
        :type keys: List[List[int]]
        :type containedBoxes: List[List[int]]
        :type initialBoxes: List[int]
        :rtype: int
        """
        n = len(status)
        visited = [False] * n  # Track if a box is already opened
        has_box = [False] * n  # Track if we have the box
        has_key = [False] * n  # Track if we have the key

        q = deque()
        for box in initialBoxes:
            has_box[box] = True
            if status[box] == 1:
                q.append(box)
                visited[box] = True

        total_candies = 0

        while q:
            box = q.popleft()
            total_candies += candies[box]

            # Process all keys found in the current box
            for key in keys[box]:
                if not has_key[key]:
                    has_key[key] = True
                    if has_box[key] and not visited[key]:
                        q.append(key)
                        visited[key] = True

            # Process all contained boxes
            for new_box in containedBoxes[box]:
                has_box[new_box] = True
                if status[new_box] == 1 or has_key[new_box]:
                    if not visited[new_box]:
                        q.append(new_box)
                        visited[new_box] = True

        return total_candies
