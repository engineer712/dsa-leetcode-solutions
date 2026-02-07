# Approach
# 1️. Maintain a stack where each element is [price, span].
# 2️. For each new price:
# Start with span = 1.
# While the stack's top price ≤ current price, pop it and add its span to the current span.
# 3️. Push [price, span] into the stack.
# 4️. Return span.


class StockSpanner(object):

    def __init__(self):
        self.stack = []
    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append((price,span))
        return span

  
