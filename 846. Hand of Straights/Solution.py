class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        # checks if the total number of cards in the hand is divisible by the group size. If it's not, it's impossible to divide the hand into groups of the specified size, so the function returns False.
        if len(hand) % groupSize != 0:
            return False
        # Counter counts the occurrences of each card in the hand and stores it as a dictionary where the keys are the card numbers and the values are their counts.
        counter = collections.Counter(hand) #({1: 1, 2: 2, 3: 2, 4: 1, 6: 1, 7: 1, 8: 1})
        #  starts a loop that iterates over each unique card number (num) in the hand, in ascending order.
        for num in sorted(counter): #[1, 2, 3, 4, 6, 7, 8].
            # retrieves the count (frequency) of the current card (num) from the Counter.
            frequency = counter[num]
            # f the frequency of the current card is zero, it means this card has already been fully used in forming previous groups, so the loop continues to the next card.  Skip Cards with Zero Frequency
            if not frequency:
                continue
            # loop tries to form a group of groupSize consecutive cards starting with num.
            for i in range(groupSize):
                # checks if there are enough cards of each required number to form the group. If any required card has fewer occurrences than the current frequency, it returns False because it's not possible to form the group.
                if counter[num + i] < frequency:
                    return False
                # reduces the count of each card in the group by the frequency of the starting card. This accounts for using those cards in the current group.
                counter[num + i] -= frequency
        # If the function has processed all the cards without returning False, it means the hand can be successfully divided into groups of consecutive cards, so it returns True.
        return True
