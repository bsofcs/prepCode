#lruCache.py
#implement LRU Cache
from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity):
        if capacity is None:
            return []
        self.lenLRU=capacity
        self.cache=[[],[]]
        self.counter=0
        self.use=[0]*capacity

    def get(self, key):
        if key is None:
            return -1
        if key in self.cache[0]:
            self.counter+=1
            indexKey=self.cache[0].index(key)
            self.use[indexKey]=self.counter
            return self.cache[1][indexKey]
        return -1

    def put(self, key, value):
        if key is None or value is None:
            return
        if key in self.cache[0]:
            self.counter+=1
            indexKey=self.cache[0].index(key)
            self.use[indexKey]=self.counter
            self.cache[0][indexKey]=key
            self.cache[1][indexKey]=value
        elif len(self.cache[0])==self.lenLRU:
            minKey=self.use.index(min(self.use))
            self.cache[0][minKey]=key
            self.cache[1][minKey]=value
            self.counter+=1
            self.use[minKey]=self.counter
        else:
            self.counter+=1
            self.use.append(self.counter)
            self.cache[0].append(key)
            self.cache[1].append(value)

class LRUCacheOD:

    def __init__(self, capacity):
        self.capacity = capacity
        self.lru_cache = OrderedDict()
        

    def get(self, key):
        if key in self.lru_cache:
            val = self.lru_cache[key]
            del self.lru_cache[key]
            self.lru_cache[key] = val
            return val
        return -1

    def put(self, key, value):
        if key in self.lru_cache:
            del self.lru_cache[key]
            self.lru_cache[key] = value
        else:
            self.lru_cache[key] = value
            if len(self.lru_cache) > self.capacity:
                self.lru_cache.popitem(last=False)    
                


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


inputCommands=["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
inputValues=[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

print(len(inputCommands),len(inputValues))
capacity=inputValues[0][0]
l=LRUCache(capacity)
print(l.cache,l.lenLRU,l.counter,l.use)