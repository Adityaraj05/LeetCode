class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse=True) #[6,5,3,1,0]
        for index, citation in enumerate(citations): #[0->6, 1->5, 2->3,3->1,4->0]
            if index >= citation:
                return index
        # if not found just simply return the len of the citations , it's given in the question
        return len(citations)
