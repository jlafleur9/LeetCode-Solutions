class TimeMap:

    def __init__(self):
        self.store = {} #Key is a string, Value is a [list of [value, timestamp ]]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        result = ""
        values = self.store.get(key, [])
        
        left = 0
        right = len(values) - 1
        
        while left <= right:
            middle = (left + right) // 2
            if values[middle][1] <= timestamp:
                result = values[middle][0]
                left = middle + 1
            else:
                right = middle - 1
        
        return result

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)