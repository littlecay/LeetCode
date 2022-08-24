class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_p = 0
        right_p = len(height)-1
        tmp = 0
        area = (right_p-left_p)*min(height[right_p],height[left_p])
        while right_p > left_p:
            if height[right_p]>height[left_p]:
                tmp = height[left_p]
                while height[left_p]<=tmp and right_p > left_p:
                    left_p = left_p + 1
                area = max(area, (right_p-left_p)*min(height[right_p],height[left_p]))
            else:
                tmp = height[right_p]
                while height[right_p]<=tmp and right_p > left_p:
                    right_p = right_p - 1
                area = max(area, (right_p-left_p)*min(height[right_p],height[left_p]))
        return area
