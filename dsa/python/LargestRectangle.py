class Solution(object):
    def largestRectangleArea(heights):
        heights = [0] + heights + [0]  # Add sentinel bars
        stack = []
        max_area = 0

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1  # distance between current and stack top after pop
                max_area = max(max_area, height * width)
            stack.append(i)

        return max_area

        
s1 = Solution()
heights = [2,1,5,6,2,3]
print(f"Orignial heights : {heights}")
print(f"The largest rectangle {s1.largestRectangleAre(heights)}")