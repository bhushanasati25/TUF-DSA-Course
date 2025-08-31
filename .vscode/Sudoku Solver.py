class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        empties = []

        def box_id(r, c):
            return (r // 3) * 3 + (c // 3)

        def bit(d):  
            return 1 << (d - 1)

        pc = [0] * 512
        for m in range(512):
            pc[m] = pc[m >> 1] + (m & 1)

        for r in range(9):
            for c in range(9):
                ch = board[r][c]
                if ch == '.':
                    empties.append((r, c))
                else:
                    d = ord(ch) - 48  
                    b = box_id(r, c)
                    m = bit(d)
                    rows[r] |= m
                    cols[c] |= m
                    boxes[b] |= m

        def candidates(r, c):
            used = rows[r] | cols[c] | boxes[box_id(r, c)]
            return (~used) & 0x1FF  

        def select():
            idx = -1
            best_mask = 0
            best_cnt = 10
            for i, (r, c) in enumerate(empties):
                if board[r][c] != '.':
                    continue
                mask = candidates(r, c)
                cnt = pc[mask]  
                if cnt == 0:
                    return i, 0, 0
                if cnt < best_cnt:
                    best_cnt = cnt
                    best_mask = mask
                    idx = i
                    if cnt == 1:
                        break
            return idx, best_mask, best_cnt

        def solve():
            for r, c in empties:
                if board[r][c] == '.':
                    break
            else:
                return True

            i, mask, _ = select()
            if i == -1 or mask == 0:
                return False

            r, c = empties[i]
            b = box_id(r, c)

            m = mask
            while m:
                lb = m & -m
                m -= lb
                d = (lb.bit_length() - 1) + 1  
                bm = bit(d)

                board[r][c] = chr(48 + d)
                rows[r] |= bm
                cols[c] |= bm
                boxes[b] |= bm

                if solve():
                    return True
                
                board[r][c] = '.'
                rows[r] ^= bm
                cols[c] ^= bm
                boxes[b] ^= bm

            return False

        solve()
