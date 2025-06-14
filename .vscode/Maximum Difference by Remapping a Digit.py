class Solution(object):
    def minMaxDifference(self, num):
        """
        :type num: int
        :rtype: int
        """
        s_num = str(num)
        max_num_str = list(s_num)
        digit_to_change_for_max = ''
        for digit in s_num:
            if digit != '9':
                digit_to_change_for_max = digit
                break
        
        if digit_to_change_for_max == '': 
            max_val = int(s_num)
        else:
            for i in range(len(max_num_str)):
                if max_num_str[i] == digit_to_change_for_max:
                    max_num_str[i] = '9'
            max_val = int("".join(max_num_str))
       
        min_num_str = list(s_num)
        digit_to_change_for_min = ''
        for digit in s_num:
            if digit != '0':
                digit_to_change_for_min = digit
                break
        
        if s_num[0] == '1': 
            for i in range(len(min_num_str)):
                if min_num_str[i] == '1':
                    min_num_str[i] = '0'
        else: 
            digit_to_change_for_min = s_num[0] 
            for i in range(len(min_num_str)):
                if min_num_str[i] == digit_to_change_for_min:
                    min_num_str[i] = '0'

        min_val = int("".join(min_num_str))
        
        return max_val - min_val