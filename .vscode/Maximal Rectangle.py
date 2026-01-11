class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * cols
        max_area = 0

        def largestRectangleArea(heights):
            stack = []
            max_area = 0
            for i in range(len(heights) + 1):
                current_height = heights[i] if i < len(heights) else 0

                while stack and current_height < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, h * width)

                stack.append(i)

            return max_area

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == '1':
                    heights[c] += 1   
                else:
                    heights[c] = 0   

            max_area = max(max_area, largestRectangleArea(heights))

        return max_area
