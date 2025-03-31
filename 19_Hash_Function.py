class HashTable:
    def __init__(self,capacity=10):
        self.capacity=capacity
        self.table=[None]*capacity
        
    def hash_function(self,key):
        return key%self.capacity
    
    def insert(self,key,value):
        index=self.hash_function(key)
        self.table[index]=(key,value)
    
    def print_Hash_Table(self):
        print("Hash Table")
        for i in range(len(self.table)):
            item=self.table[i]
            if item:
                print(f"index: {i}, key:{item[0]}, value:{item[1]}")

if __name__=="__main__":
    table=HashTable()
    table.insert(123,456000)
    table.insert(456,789000)
    table.insert(789,1011112000)
    table.print_Hash_Table()