class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        x1, y1 = points[0]
        x2, y2 = points[1]
        x3, y3 = points[2]
        # if three points are non collinear then they form triangle. So all we need to check if the area of the triangle formed is non-zero. If the area is zero it means all three points are collinear.
        area = 0.5*(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))
        return area != 0
        
