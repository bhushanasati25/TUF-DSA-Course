class Fancy(object):

    def __init__(self):
        self.seq = []
        self.A = 1
        self.B = 0
        self.A_inv = 1
        self.MOD = 10**9 + 7

    def append(self, val):
        """
        :type val: int
        :rtype: None
        """
        x0 = ((val - self.B) * self.A_inv) % self.MOD
        self.seq.append(x0)

    def addAll(self, inc):
        """
        :type inc: int
        :rtype: None
        """
        self.B = (self.B + inc) % self.MOD

    def multAll(self, m):
        """
        :type m: int
        :rtype: None
        """
        self.A = (self.A * m) % self.MOD
        self.B = (self.B * m) % self.MOD
        self.A_inv = (self.A_inv * pow(m, self.MOD - 2, self.MOD)) % self.MOD

    def getIndex(self, idx):
        """
        :type idx: int
        :rtype: int
        """
        if idx >= len(self.seq):
            return -1
        return (self.A * self.seq[idx] + self.B) % self.MOD