class MyHashSet:

    def __init__(self):
        self.hashh = {}
        

    def add(self, key: int) -> None:
        self.hashh[key] = 1
        
        
        

    def remove(self, key: int) -> None:
        if key in self.hashh:
            self.hashh.pop(key)
            
        

    def contains(self, key: int) -> bool:
        if key in self.hashh:
            return True
        else:
            return False
        
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)