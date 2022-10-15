class Hash:
    #constructor with a capacity of 40
    #assign all buckets as an empty list
    # O(N)
    def __init__(self, capacity=40):
        self.table = []
        for i in range(capacity):
            self.table.append([])
    #O(1) return package as an int
    def hash_funct(self, package):
        return int(package)
        
        
        
    #insert package into chain bucket
    # O(1)   
    def insert(self, package, data):
        bucket = self.hash_funct(package) % len(self.table)
        bucket_list = self.table[bucket]

        #appends to end of bucket lsit
        bucket_list.append(data)
    #O(1)
    def search(self, key):
    #use key to hash bucket value
        bucket = self.hash_funct(key) % len(self.table)
        bucket_list = self.table[bucket]
    #get the number of items in the list if more than one
    #search item in the selected bucket:
        #if data in bucket_list:
        #    item_index = bucket_list.index(data)
        if bucket_list[0][0] == key:    
            return bucket_list[0]
        else:
            return None
    #O(1)
    def delete(self, key, data):
        bucket = self.hash_funct(key) % len(self.table)
        bucket_list = self.table[bucket]

        if data in bucket_list:
            bucket_list.remove(data)