class Robot(object):

    def __init__(self, width, height):
        self.w = width
        self.h = height
        self.pos = 0
        self.moved = False
        self.mod = 2 * (width + height) - 4
        self.path = []
        
        for x in range(width):
            self.path.append(((x, 0), "East"))
        for y in range(1, height):
            self.path.append(((width - 1, y), "North"))
        for x in range(width - 2, -1, -1):
            self.path.append(((x, height - 1), "West"))
        for y in range(height - 2, 0, -1):
            self.path.append(((0, y), "South"))

    def step(self, num):
        self.moved = True
        self.pos = (self.pos + num) % self.mod

    def getPos(self):
        return list(self.path[self.pos][0])

    def getDir(self):
        if self.moved and self.pos == 0:
            return "South"
        return self.path[self.pos][1]

# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()