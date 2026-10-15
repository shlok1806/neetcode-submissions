class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        diff = [0] * 1001
        for n, start, end in trips:
            diff[start] += n
            diff[end] -= n
        curr = 0
        for d in diff:
            curr += d
            if curr > capacity:
                return False
        return True