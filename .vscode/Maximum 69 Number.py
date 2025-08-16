class Solution(object):
    def maximum69Number(self, num):
        """
        :type num: int
        :rtype: int
        """
        # Convert to string, replace the first '6' with '9', and convert back
        return int(str(num).replace('6', '9', 1))
