from collections import defaultdict
import struct
import time

index_file = 'index.index'
data_file = 'wikipedia_sample.txt'


def get_index():
    index_data = {}

    with open(data_file, 'r', encoding='utf-8') as data_f:
        for line in data_f:
            text = line.split()

            # for word in set(text[1:]):
            #     if word in index_data:
            #         index_data[word].append(int(text[0]))
            #     else:
            #         index_data[word] = [int(text[0]), ]

            for word in set(text[1:]):
                index_data.setdefault(word, []).append(int(text[0]))

    return index_data


def save_inverted_index(index_data):
    with open('inv.index', 'wb') as inverted_index:
        # write length of dict
        length = len(index_data)
        d = struct.pack('>i', length)
        inverted_index.write(d)

        for word in index_data:
            # write length of word
            w_length = len(word)
            key_len = struct.pack('>h', w_length)
            inverted_index.write(key_len)

            # write packed word
            bt_word = word.encode()
            bt_word_packed = struct.pack('>' + str(w_length) + 's', bt_word)
            inverted_index.write(bt_word_packed)

            # write length of values list
            val_len = struct.pack('>h', len(index_data[word]))
            inverted_index.write(val_len)

            # write each element of list
            for doc_id in index_data[word]:
                doc_id_packed = struct.pack('>h', doc_id)
                inverted_index.write(doc_id_packed)


def load_inverted_index():
    index_data = {}

    with open('inv.index', 'rb') as inverted_index:
        # get index_data length
        inv_index_len = struct.unpack('>i', inverted_index.read(4))[0]

        i = 0
        while i < inv_index_len:
            # get word
            d_word_len = inverted_index.read(2)
            word_len = struct.unpack('>h', d_word_len)[0]
            d_word = inverted_index.read(word_len)
            word = struct.unpack('>' + str(word_len) + 's', d_word)[0].decode()

            # get list of values
            d_val_len = inverted_index.read(2)
            val_len = struct.unpack('>h', d_val_len)[0]
            d_values = inverted_index.read(2 * val_len)
            values = struct.unpack('>' + str(val_len) + 'h', d_values)
            documents = list(values)

            index_data[word] = documents
            print(f'{word}: {documents}')
            i += 1

    return index_data


def save_index(index_data):
    index_raw = b''
    large_data = ''

    i = 0

    for word in index_data:
        # fmt = 's' + ''.join(['h' for n in INDEX_DATA[word]])
        # index_raw += struct.pack(fmt, word.encode('utf-8'), *INDEX_DATA[word]) + b'\n'
        index_raw += ('\n' + word).encode('utf-8') + struct.pack(''.join(['h' for n in index_data[word]]),
                                                                 *index_data[word])

        large_data += '{0}: {1}\n'.format(word, index_data[word])

        i += 1
        # if i >= 1000:
        #     break
        print('{0}%...'.format(100 * i / len(index_data)), end='\r')

    with open(index_file, 'bw') as index_f:
        index_f.write(index_raw)

    with open('without_compression.txt', 'w') as index_f:
        index_f.write(large_data)


start_get_index = time.time()
# i_data = get_index()
# print(len(i_data))
print(f'get_index took {time.time() - start_get_index} sec.')
# save_index(i_data)
# save_inverted_index(i_data)
i_data = load_inverted_index()
print(len(i_data))

# 18.487 sec = index data as global
# 17.976 sex = index data as func variable
