class OrderedStream:

    def __init__(self, n: int):
        self.a = [None]*n
        self.start = -1
        self.handled = 0
        
        
        

    def insert(self, idKey: int, value: str) -> List[str]:
        self.a[idKey-1] = value
        
        if idKey == 1 :
            self.start = 0
        
        res = []
        if self.start != -1 :
            for i,item in enumerate(self.a[self.start:]) : 
                if item is None:
                    self.start = i+self.start
                    break
                res+= [item]
                
        return res


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)