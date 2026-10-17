class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        res = [0] * len(price)
        self.stack = []

        for i,p in enumerate(price):
            while self.stack and p <= self.stack[-1][0]:
                stackPrice, stackIndex = self.stack.pop()
                res[stackIndex] = i - stackIndex
            self.stack.append([p,i])

        if num in res:
            if num == 0:
                num is None
        return res


        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)