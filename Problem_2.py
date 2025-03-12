#In this we intialize the first bucket with size 1000. In case of put we first we hash the key and get the first bucket then calculate second hash 
# and keep the value there.
# In case of get we calculate both the hash and then return it
# In case of remove we calculate both the hash and assign the calculate location as None
#Time Complexity = O(1)
#Space Complexity = O(1)

class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.bucket = [None]*self.size

    def put(self, key: int, value: int) -> None:
        first_hash = key % self.size
        second_hash = key // self.size
        if not self.bucket[first_hash]:
            self.bucket[first_hash] = [None]*(self.size+1)
        self.bucket[first_hash][second_hash] = value

        

    def get(self, key: int) -> int:
        first_hash = key % self.size
        second_hash = key // self.size
        return self.bucket[first_hash][second_hash] if self.bucket[first_hash] and self.bucket[first_hash][second_hash] is not None else -1
        

    def remove(self, key: int) -> None:
        first_hash = key % self.size
        second_hash = key // self.size
        if self.bucket[first_hash]:
            self.bucket[first_hash][second_hash] = None
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)