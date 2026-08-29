class Solution:
    def maxArea(self, heights: List[int]) -> int:
        a=0
        b=len(heights)-1
        m=0
        while(a<b):
            w=b-a
            h=min(heights[a],heights[b])
            area=w*h
            m=max(m,area)
            if heights[a]<heights[b]:
                a+=1
            else:
                b-=1
        return m
        