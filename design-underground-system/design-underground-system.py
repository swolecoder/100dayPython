class UndergroundSystem:

    def __init__(self):
        self.i = defaultdict(tuple)
        self.o = defaultdict(list)
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.i[id] = (stationName,t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation , startTime = self.i[id]
        totaltime = t- startTime
        
        self.o[(startStation,stationName)].append(totaltime)
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        
        return sum(self.o[(startStation,endStation)])/len(self.o[(startStation,endStation)])
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)