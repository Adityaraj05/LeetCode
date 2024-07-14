class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        horizontal = len(horizontalCut)
        vertical = len(verticalCut) 
        # sorting in descending order beacuse it help us in miniming the cost of pieces.
        horizontalCut.sort(reverse=True)
        verticalCut.sort(reverse=True)

        # taking two pointer hori and vertical for making traversal in the cake 
        hori, ver = 0, 0
        horizontalPieces, verticalPieces = 1, 1

        total_cost = 0

        while hori < horizontal and ver < vertical:
            if horizontalCut[hori] >= verticalCut[ver]:
                total_cost += horizontalCut[hori] * verticalPieces # horizontal cut ko vertical Pieces se multiply karnge
                horizontalPieces +=1
                hori +=1
            else:
                total_cost += verticalCut[ver] * horizontalPieces # verticalCut ko horizontal Pieces se multiply karnge
                verticalPieces +=1
                ver +=1
        
        # now check if any one of the either hori and ver are left to traverse.
        while hori < horizontal:
            total_cost += horizontalCut[hori] * verticalPieces
            horizontalPieces +=1
            hori +=1
        
        while ver < vertical:
            total_cost += verticalCut[ver] * horizontalPieces
            verticalPieces +=1
            ver +=1

        return total_cost





        
