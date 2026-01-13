class Solution(object):
    def separateSquares(self, squares):
        """
        :type squares: List[List[int]]
        :rtype: float
        """
        half_area = sum(l * l for _, _, l in squares) / 2.0
        
        events = []
        for _, y, l in squares:
            events.append((y, l))        
            events.append((y + l, -l)) 
        
        events.sort()
        
        current_width = 0.0
        area_so_far = 0.0
        prev_y = events[0][0]
        
        for y, delta in events:
            height = y - prev_y
            if height > 0 and current_width > 0:
                area_gain = current_width * height
                
                if area_so_far + area_gain >= half_area:
                    return prev_y + (half_area - area_so_far) / current_width
                
                area_so_far += area_gain
            
            current_width += delta
            prev_y = y
        
        return float(prev_y)
