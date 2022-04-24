class UndergroundSystem:

    def __init__(self):
        self.hash_in = {}
        self.pair = collections.defaultdict(lambda : (0,0))
        
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        assert(id not in self.hash_in)
        self.hash_in[id] = (stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        assert(id in self.hash_in)
        prevstn, prevtime = self.hash_in[id]
        prevtotal, prevcount = self.pair[(prevstn, stationName)]
        new_total = prevtotal + t - prevtime
        new_count = prevcount + 1
        
        self.pair[prevstn, stationName] = new_total, new_count
        del self.hash_in[id]
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, count = self.pair[(startStation, endStation)]
        assert count > 0
        
        return total / count
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)