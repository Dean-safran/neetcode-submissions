class TimeMap:
    """

    data structure is of the form ->
    {key : [(timestamp1, val) , (timestamp2, val), ]}
    where the timestamps are inserted in order (append to the end)

    set just appends a timestamp

    get retrives list of key, then binary searches for 
    the first smallest timestamp (or equivalent timestamp)

    """

    def bin_search(self, l, r, timestamp, arr) : 
        if l > r :
            return r
        
        m = (l + r) // 2

        if arr[m][0] == timestamp :
            return m
        elif arr[m][0] > timestamp :
            return self.bin_search(l, m-1, timestamp, arr)
        elif arr[m][0] < timestamp :
            return self.bin_search(m+1, r, timestamp, arr)

 
    def __init__(self):
        self.timestamps = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timestamps :
            self.timestamps[key] = [(timestamp, value)]
        else : 
            self.timestamps[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timestamps :
            return ""
        else : 
            arr_to_search = self.timestamps[key]
            res_idx = self.bin_search(0, len(arr_to_search) - 1, timestamp, arr_to_search)
            if res_idx == -1 : 
                return ""
            return arr_to_search[res_idx][1]
