import struct


INDEX_DATA = {}
index_file = 'index.index'
data_file = 'data.txt'


def get_index():
    global INDEX_DATA

    with open(data_file, 'r') as data_f:
        for line in data_f:
            text = line.split()

            for word in set(text[1:]):
                if word in INDEX_DATA:
                    INDEX_DATA[word].append(int(text[0]))
                else:
                    INDEX_DATA[word] = [int(text[0]), ]


words_separator = b'_!<'
word_fmt_separator = b'_>>'
list_separator = b'!$>'

def save_index():
    global INDEX_DATA

    with open(index_file, 'wb') as index_f:
        for word, numbers in INDEX_DATA.items():
            index_f.write(words_separator)
            index_f.write(word.encode('utf8'))
            index_f.write(word_fmt_separator)
            index_f.write(str(len(numbers)).encode('utf8'))  # set number here
            index_f.write(list_separator)
            index_f.write(struct.pack('H'*len(numbers), *numbers))


def load_index():
    global INDEX_DATA

    INDEX_DATA = {}

    with open(index_file, 'rb') as index_f:
        data = index_f.read()

        words_data = data.split(words_separator)

        for d in words_data[1:]:
            word = d.split(word_fmt_separator)[0]
            count = int(d.split(word_fmt_separator)[1].split(list_separator)[0].decode('utf8'))
            numbers = d.split(list_separator)[1]

            INDEX_DATA[word] = struct.unpack('H'*count, numbers)



get_index()
print(len(INDEX_DATA))
save_index()

load_index()

print(len(INDEX_DATA))
