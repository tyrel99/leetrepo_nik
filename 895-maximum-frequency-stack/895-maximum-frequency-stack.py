class FreqStack:

    def __init__(self):
        self.hashh = {}
        self.max_freq = 0
        self.stack = {}
        

    def push(self, val: int) -> None:
        Valcnt = 1 + self.hashh.get(val,0)
        self.hashh[val] = Valcnt
        
        if Valcnt > self.max_freq:
            self.max_freq = Valcnt
            self.stack[Valcnt] = []
        self.stack[Valcnt].append(val)
        

    def pop(self) -> int:
        res = self.stack[self.max_freq].pop()
        self.hashh[res] -= 1
        if not self.stack[self.max_freq]:
            self.max_freq -= 1
        return res
            
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()