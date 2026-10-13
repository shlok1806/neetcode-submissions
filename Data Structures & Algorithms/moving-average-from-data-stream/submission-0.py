class MovingAverage:

    def __init__(self, size: int):
        self.windowSize = size
        self.arr = []

    def next(self, val: int) -> float:
        self.arr.append(val)

        avg = 0 
        count = 0
        for i in range(len(self.arr) -1, max(-1, len(self.arr)- 1 - self.windowSize), -1):         
            count += 1
            avg += self.arr[i]

        return avg/count


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
