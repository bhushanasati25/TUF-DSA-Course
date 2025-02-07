import bisect

class ContinuousIntensityBST:
    def __init__(self):
        self.segs = []
    
    def get(self, x):
        i = bisect.bisect_right(self.segs, [x, float('inf')]) - 1
        if i < 0:
            return 0
        return self.segs[i][1]
    
    def _ensure_boundary(self, x):
        i = bisect.bisect_left(self.segs, [x, -10**9])
        if i < len(self.segs) and self.segs[i][0] == x:
            return  # Already a breakpoint.
        val = self.get(x)
        self.segs.insert(i, [x, val])
    
    def _merge(self):
        if not self.segs:
            return
        new_segs = [self.segs[0]]
        for i in range(1, len(self.segs)):
            if i == len(self.segs) - 1:
                new_segs.append(self.segs[i])
            else:
                if self.segs[i][1] != new_segs[-1][1]:
                    new_segs.append(self.segs[i])
        if new_segs and new_segs[0][1] == 0:
            new_segs.pop(0)
        self.segs = new_segs
    
    def add(self, frm, to, amount):
        if frm >= to or amount == 0:
            return
        self._ensure_boundary(frm)
        self._ensure_boundary(to)
        i = bisect.bisect_left(self.segs, [frm, -10**9])
        while i < len(self.segs) and self.segs[i][0] < to:
            self.segs[i][1] += amount
            i += 1
        self._merge()
    
    def set(self, frm, to, value):
        if frm >= to:
            return
        self._ensure_boundary(frm)
        self._ensure_boundary(to)
    
        i = bisect.bisect_left(self.segs, [frm, -10**9])
        j = bisect.bisect_left(self.segs, [to, -10**9])
       
        del self.segs[i+1:j]
      
        self.segs[i][1] = value
        
        k = bisect.bisect_left(self.segs, [to, -10**9])
        if k < len(self.segs) and self.segs[k][0] == to:
            self.segs[k][1] = 0
        else:
            self.segs.insert(k, [to, 0])
        self._merge()
    
    def display(self):
        print(self.segs)
