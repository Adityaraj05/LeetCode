class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        sort_heights = sorted(heights)
        count = 0
        i = 0
        while i < len(heights):
            if sort_heights[i] != heights[i]:
                count +=1
            i +=1
        return count

