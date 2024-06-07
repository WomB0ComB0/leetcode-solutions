# Given a non-negative integers representing an elevation map where the width of each bar is 1, computer how much water it can trap after raining
from typing import List
class Solutiontrap:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res


# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map(black section) is represented bty array [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2]
# 6 units of rain water are trapped (blue section are being trapped).
