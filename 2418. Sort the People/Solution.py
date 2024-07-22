class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        name_to_height = {}
        # with the help of zip function we can iterate over two array simaltenously.
        for name, height in zip(heights, names):
            name_to_height[name] = height   # ["Mary" -> 180; "John"-> 165; "Emma"-> 170] 
        result = []
        for h in reversed(sorted(heights)): # ["Mary" -> 180; "Emma"-> 170; "John"-> 165]
            result.append(name_to_height[h])
            

        return result


         


        
