class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #maximize area of a rectangle.
        #maximize distance and height
        #two pointers
        #[1,7,2,5,4,7,3,6]
          #0,1,2,3,4,5,6,7
        # for example:
        current = 0
        max_area = 0
        l, r = 0, len(heights) - 1
        while l < r:
            distance = r - l
            area = min(heights[l], heights[r]) * distance
            max_area = max(max_area, area)
            #determine limiting factor, and move the other one
            #how to determine limiting factor:
            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
        return max_area


        