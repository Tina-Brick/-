class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        #OrderedDict preserves the order in which the keys are inserted
        self.dic=collections.OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        #delete and reinsert the key(to the top)
        #pop-if key is in the dictionary, remove it and return its value
        value=self.dic.pop(key)
        self.dic[key]=value
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic.pop(key)
        else:
            if self.capacity>0:
                self.capacity-=1
            else:
            # if full, pop the least frequent used item
                self.dic.popitem(last=False)
        self.dic[key]=value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
