from bisect import bisect_left

class IntensityManager:
    def __init__(self):
        self.segments = {}
        self.segments[-float('inf')] = (0, False)
    
    def _get_sorted_keys(self):
        return sorted(self.segments.keys())
    
    def _merge_segments(self):
       
        keys = self._get_sorted_keys()
        if not keys:
            return
        new_segments = {}
        new_segments[keys[0]] = self.segments[keys[0]]
        
     
        for key in keys[1:-1]:
            curr_intensity, curr_explicit = self.segments[key]
           
            prev_key = list(new_segments.keys())[-1]
            prev_intensity, _ = self.segments[prev_key]
            if curr_explicit or (curr_intensity != prev_intensity):
                new_segments[key] = self.segments[key]
        
        if len(keys) > 1:
            new_segments[keys[-1]] = self.segments[keys[-1]]
        
        self.segments = new_segments

    def add(self, frm, to, amount):
        
        if frm >= to:
            return  

        if frm not in self.segments:
            prev_key = max(k for k in self.segments if k < frm)
            prev_intensity, _ = self.segments[prev_key]
            self.segments[frm] = (prev_intensity, True)
        
        if to not in self.segments:
            prev_key = max(k for k in self.segments if k < to)
            prev_intensity, _ = self.segments[prev_key]
            self.segments[to] = (prev_intensity, True)
        
        keys = self._get_sorted_keys()
        for key in keys:
            if key >= to:
                break
            if key >= frm:
                curr_intensity, curr_explicit = self.segments[key]
                self.segments[key] = (curr_intensity + amount, curr_explicit)
        
        self._merge_segments()
    
    def set(self, frm, to, amount):
        
        if frm >= to:
            return 
        
        if frm not in self.segments:
            prev_key = max(k for k in self.segments if k < frm)
            prev_intensity, _ = self.segments[prev_key]
            self.segments[frm] = (prev_intensity, True)
        if to not in self.segments:
            prev_key = max(k for k in self.segments if k < to)
            prev_intensity, _ = self.segments[prev_key]
            self.segments[to] = (prev_intensity, True)
        
        old_intensity = self.segments[max(k for k in self.segments if k < to)][0]
        
        keys = self._get_sorted_keys()
        for key in keys:
            if frm < key < to:
                del self.segments[key]
        
        self.segments[frm] = (amount, True)
     
        self.segments[to] = (old_intensity, True)
        
        self._merge_segments()
    
    def get_segments(self):
        keys = self._get_sorted_keys()
        return [[key, self.segments[key][0]] for key in keys if key != -float('inf')]
    
    def display(self):
        print(self.get_segments())