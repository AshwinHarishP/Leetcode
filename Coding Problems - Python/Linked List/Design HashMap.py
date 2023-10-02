class MyHashMap(object):

    def __init__(self):
        self.hashmap = {}

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        self.hashmap[key] = value

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.hashmap:

            return self.hashmap.get(key) 
        return -1  

        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key in self.hashmap:

            self.hashmap.pop(key,None)  # Returns None(default value) if key is not present in hashmap
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
