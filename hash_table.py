class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)  # 23 is a prime number; any prime can be used
        return my_hash

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:  # create list if index value has None, otherwise just append.
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index]:  # create list if index value has None, otherwise just append.
            for i in range(len(self.data_map[index])):  # iterate through the list inside specific index (NOT data map)
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None


my_hash = HashTable()

my_hash.set_item('bolts', 1400)
my_hash.set_item('washers', 120)

print(my_hash.get_item('bolts'))
print(my_hash.get_item('washers'))
print(my_hash.get_item('lumber'))


my_hash.print_table()

