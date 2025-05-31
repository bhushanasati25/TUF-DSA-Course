from collections import deque

class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        n = len(board)

        # Convert label to coordinates on the board
        def label_to_coords(label):
            row_from_bottom = (label - 1) // n
            r = n - 1 - row_from_bottom
            if row_from_bottom % 2 == 0:
                c = (label - 1) % n
            else:
                c = n - 1 - (label - 1) % n
            return r, c

        visited = [False] * (n * n + 1)
        queue = deque()
        queue.append((1, 0))  # (label, moves)
        visited[1] = True

        while queue:
            label, moves = queue.popleft()
            if label == n * n:
                return moves
            for i in range(1, 7):
                next_label = label + i
                if next_label > n * n:
                    continue
                r, c = label_to_coords(next_label)
                if board[r][c] != -1:
                    next_label = board[r][c]
                if not visited[next_label]:
                    visited[next_label] = True
                    queue.append((next_label, moves + 1))

        return -1
