class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """

        # here i am using hashset because comparison will become fast O(1).
        Hashsetarr2 = set(arr2)
        Hashmaparr1 = defaultdict(int)
        end = []
        for num in arr1:
            if num not in Hashsetarr2:
                end.append(num)
            Hashmaparr1[num] +=1 #({2:3, 3:2, 1:1, 4:1, 6:1,9:1})
        end.sort() #[7,19]
        result = []
        for num in arr2:
            for i in range(Hashmaparr1[num]):
                result.append(num)
        return result + end

