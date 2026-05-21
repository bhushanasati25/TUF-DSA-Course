class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res = []
        cur_line = []
        num_of_letters = 0
        
        for word in words:
            if num_of_letters + len(word) + len(cur_line) > maxWidth:
                total_spaces = maxWidth - num_of_letters
                for i in range(total_spaces):
                    cur_line[i % (len(cur_line) - 1 or 1)] += ' '
                    
                res.append(''.join(cur_line))
                cur_line = []
                num_of_letters = 0
                
            cur_line.append(word)
            num_of_letters += len(word)
            
        last_line = ' '.join(cur_line)
        last_line += ' ' * (maxWidth - len(last_line))
        res.append(last_line)
        
        return res