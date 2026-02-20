class Solution(object):
    def makeLargestSpecial(self, s):
        count = 0
        i = 0
        substrings = []
        
        for j, char in enumerate(s):
            count += 1 if char == '1' else -1
            
            if count == 0:
                inner = self.makeLargestSpecial(s[i+1:j])
                substrings.append('1' + inner + '0')
                i = j + 1
                
        substrings.sort(reverse=True)
        return "".join(substrings)