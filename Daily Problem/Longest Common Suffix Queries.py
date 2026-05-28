class TrieNode:
    def __init__(self):
        self.children = {}
        self.best_idx = -1
        self.min_len = float('inf')

class Solution(object):
    def stringIndices(self, wordsContainer, wordsQuery):
        """
        :type wordsContainer: List[str]
        :type wordsQuery: List[str]
        :rtype: List[int]
        """
        root = TrieNode()
        
        for i, word in enumerate(wordsContainer):
            n = len(word)
            
            if n < root.min_len:
                root.min_len = n
                root.best_idx = i
                
            curr = root
            for c in reversed(word):
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
                
                if n < curr.min_len:
                    curr.min_len = n
                    curr.best_idx = i
                    
        ans = []
        for query in wordsQuery:
            curr = root
            for c in reversed(query):
                if c not in curr.children:
                    break
                curr = curr.children[c]
            
            ans.append(curr.best_idx)
            
        return ans