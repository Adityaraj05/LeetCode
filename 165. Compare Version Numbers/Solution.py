class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        def SplitIntoInteger(version):
            return list(map(int, version.split(".")))
        v1 = SplitIntoInteger(version1) #1.2.3  ---> after spliting into integer -->[1, 2, 3]
        v2 = SplitIntoInteger(version2) #1.2.4  ---> after spliting into integer -->[1, 2, 4]
        # addding zeroes at the empty place if v1 is less than v2 as per description given in the question
        while len(v1) < len(v2):
            v1.append(0)
         # addding zeroes at the empty place if v2 is less than v2 as per description given in the question
        while len(v2) < len(v1):
            v2.append(0)
        # In this loop we are traversing each version simaltenously and comapring and according to that returning the value  
        for string1, string2 in zip(v1, v2): #string1:[1, 2, 4] and string2:[1, 2, 4]
            if string1 < string2:
                return -1
            if string1 > string2:
                return 1
        return 0
