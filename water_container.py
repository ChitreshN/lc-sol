class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        cur = 0
        res = 0

        while(i < j):
            cur = (j-i)*min(height[i],height[j])
            res = max(cur,res)
            if (height[i]> height[j]):
                j -= 1
            else:
                i += 1
        return res
