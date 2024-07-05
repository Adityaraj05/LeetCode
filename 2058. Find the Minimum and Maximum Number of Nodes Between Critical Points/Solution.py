# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev, curr, nxt = head, head.next, head.next.next # pointers to navigate through the linked list.
        distance = 1 # keeps track of the position (1-based index) of the current node being examined.
        first_critical_node = 0 #stores the position of the first critical point found.
        last_critical_node = float("-inf") #stores the position of the most recent critical point found.
        minDist = float("inf") # stores the minimum distance between any two critical points found.
        
        while nxt:
            # checks for a local maximum. or checks for a local minimum.
            if (prev.val < curr.val > nxt.val) or (prev.val > curr.val < nxt.val):
                # First Critical Point Initialization:If first_critical_node is not set (i.e., it's 0), it's set to the current distance.


                if not first_critical_node: # it will stor the first_critical_node index which help us in last to calculate the maxDist = last_critical_node - first_critical_node
                    first_critical_node = distance
                else:
                    # If first_critical_node is already set, it means there has been at least one critical point found previously. The minimum distance minDist is updated with the distance between the current critical point and the previous one (distance - last_critical_node).
                    minDist = min(minDist, distance - last_critical_node)
                
                last_critical_node = distance
            
            prev, curr, nxt = curr, nxt, nxt.next
            distance += 1
        #  checks if there were no critical points found (first_critical_node is still 0) or if there was only one critical point (i.e., the first and last critical points are the same). If either condition is true, it returns [-1, -1].
        if not first_critical_node or first_critical_node == last_critical_node:
            return [-1, -1]
        
        return [minDist, last_critical_node - first_critical_node]


                    
        
