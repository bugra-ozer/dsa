class MyHashSet:

    def __init__(self):
        self.keys={}
        self.idx=0

    def add(self, key: int) -> None:
        self.idx+=1
        self.keys[key]=self.idx

    def remove(self, key: int) -> None:
        try:
            self.keys.pop(key)
        except:
            pass

    def contains(self, key: int) -> bool:
        if key in self.keys:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)