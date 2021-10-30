from heapq import heapify,heappop,heappush
class SeatManager:

    def __init__(self, n: int):
        self.data = [i for i in range(1, n+1)]
        

    def reserve(self) -> int:
        return heappop(self.data)
        

    def unreserve(self, seatNumber: int) -> None:
        return heappush(self.data,seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)