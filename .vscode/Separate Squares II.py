class Solution(object):
    def separateSquares(self, squares):
        """
        :type squares: List[List[int]]
        :rtype: float
        """
        unique_x = set()
        for x, y, l in squares:
            unique_x.add(x)
            unique_x.add(x + l)
        
        sorted_x = sorted(list(unique_x))
        x_map = {val: i for i, val in enumerate(sorted_x)}
        m = len(sorted_x)
        
        count = [0] * (4 * m)
        length = [0.0] * (4 * m)

        def update(node, start, end, l, r, val):
            if l >= r:
                return

            if l == start and r == end:
                count[node] += val
            else:
                mid = (start + end) // 2
                if l < mid:
                    update(2 * node, start, mid, l, min(r, mid), val)
                if r > mid:
                    update(2 * node + 1, mid, end, max(l, mid), r, val)
            
            if count[node] > 0:
                length[node] = float(sorted_x[end] - sorted_x[start])
            else:
                if end - start == 1:
                    length[node] = 0.0
                else:
                    length[node] = length[2 * node] + length[2 * node + 1]

        events = []
        for x, y, l in squares:
            events.append((y, 1, x, x + l))
            events.append((y + l, -1, x, x + l))
        
        events.sort(key=lambda e: e[0])

        total_area = 0.0
        prev_y = events[0][0]
        
        for y, type_, x1, x2 in events:
            current_active_width = length[1] 
            total_area += current_active_width * (y - prev_y)
            
            update(1, 0, m - 1, x_map[x1], x_map[x2], type_)
            prev_y = y
            
        target_area = total_area / 2.0

        count = [0] * (4 * m)
        length = [0.0] * (4 * m)
        
        current_area = 0.0
        prev_y = events[0][0]
        
        for y, type_, x1, x2 in events:
            width = length[1]
            slice_area = width * (y - prev_y)
            
            if current_area + slice_area >= target_area:
                diff = target_area - current_area
                return prev_y + (diff / width if width > 0 else 0)
            
            current_area += slice_area
            update(1, 0, m - 1, x_map[x1], x_map[x2], type_)
            prev_y = y
            
        return float(prev_y)