class StockSpanner:
    def __init__(self):
        # self.stack is an attribute of the class instance. It's initialized as an empty list. pair: (price, span) indicates the structure of each element that will be stored in the stack. Each element is a tuple consisting of two values: a price and a span.
        self.stack = []  

    def next(self, price: int) -> int:
        # Initializes the span variable to 1. The span represents how many consecutive days prior to the current day that the price was less than or equal to the current day's price. and by default we kept it as a 1
        span = 1
        # This while loop continues as long as the stack is not empty and the price on top of the stack (the most recent price) is less than or equal to the current price.
        while self.stack and self.stack[-1][0] <= price:
            # It updates the span by adding the span value of the top element of the stack.
            span += self.stack[-1][1]
            # It removes the top element of the stack using self.stack.pop().
            self.stack.pop()
            # After the while loop, it appends a tuple (price, span) to the stack. This tuple represents the current price and its associated span.
        self.stack.append((price, span))
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
