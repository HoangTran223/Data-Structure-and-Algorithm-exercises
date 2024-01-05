"""Hasing with chaining. This method has not concept of rehasing.
Ở đây phần tử gọi trước sẽ gần mảng hơn, khác so với giáo trình, và cũng tiện hơn"""
BUCKET_SIZE = 7

class Hash():                    # Các biến có __ ở trước là biến "riêng tư" mà người dùng bên ngoài lớp không nên truy cập.
                                 # Dù nó vẫn có thể truy cập, nhưng đây như là 1 tiêu chuẩn code, tương tự hằng số thì nên viết hoa.
    def __init__(self, bucket):
        self.__bucket = bucket                          # Number of buckets
        self.__table = [[] for _ in range(bucket)]      # Hash table
    
    def hash_function(self, key):
        return key % self.__bucket

    def insert(self, key):
        index = self.hash_function(key)
        self.__table[index].append(key)

    def delete(self, key):
        index = self.hash_function(key)
        if key not in self.__table[index]:
            return              # Actually, it's return None, use when function not return a value
                                # Or the return value is not important
        self.__table[index].remove(key)
    
    def display_hash_table(self):
        for i in range(self.__bucket):
            print(i, end = '')
            for x in self.__table[i]:
                print(f"--> {x}", end ='')
            print()

array = [15, 11, 8, 64, 27, 13, 54, 76, 3]
h = Hash(BUCKET_SIZE)
for x in array:
    h.insert(x)
key = 15
h.delete(key)
h.display_hash_table()