class SnapshotArray:

    def __init__(self, length: int):
        self.snap_id = -1 # each time we get, find the last snap_id in the record
        self.record = [[[-1,0]] for _ in range(length)]
        # print(self.record)

    def set(self, index: int, val: int) -> None:
        self.record[index].append([self.snap_id + 1, val])
        # print(self.record)

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id

    def get(self, index: int, snap_id: int) -> int:
        i = bisect.bisect(self.record[index], [snap_id + 1]) - 1 # since bisect is always find the next right index of position, all left part is strictly less than that number
        return self.record[index][i][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
