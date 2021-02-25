# This is the very simple implementation of hashtable
# data structure based on the video from
# https://www.youtube.com/watch?v=54iv1si4YCM
#


class HashTable(object):
    size = 1000
    elements = [[] for i in range(size)]

    def get_hash(self, key: str) -> int:
        hash_value = 0

        for character in key:
            hash_value += ord(character)

        return int(hash_value % self.size)

    def __setitem__(self, key: str, value):
        element_hash = self.get_hash(key)
        is_hash_already_exists = False

        for i, element in enumerate(self.elements[element_hash]):
            if key == element[0]:
                self.elements[element_hash][i] = (key, value)
                is_hash_already_exists = True

        if not is_hash_already_exists:
            self.elements[element_hash].append((key, value))

    def __getitem__(self, key: str):
        element_hash = self.get_hash(key)

        for element in self.elements[element_hash]:
            if element[0] == key:
                return element[1]

        raise IndexError('No such element in the Hashtable!', key)


t = HashTable()
print(t.get_hash('Test'))
print(t.get_hash('ERROR'))

print('^' * 20)

t['test'] = 3
t['test'] = 4
print(t['test'], t['test'], t['ERROR'])
