class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.timeMap.get(key, None)
        if arr == None:
            return ""
        
        hi, lo = len(arr) - 1, 0 
        while hi >= lo:
            mid = (hi + lo) // 2

            if arr[mid][1] == timestamp:
                return arr[mid][0]
            if arr[mid][1] > timestamp:
                hi = mid - 1
            else: 
                lo = mid + 1

        if hi < 0:
            return ""
        return arr[hi][0]

