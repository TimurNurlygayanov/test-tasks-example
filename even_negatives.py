# Given a string ('source') and an array of strings ('negative_words'), find the number of
# appearances of negative words in the source string. Return true if the number is even (e.g. 0, 2,
# 4..) and false otherwise. Note that input strings are case insensitive. If any negative word (e.g.
# 'no') is a substring of another (e.g. ‘not’), count 1.
# even_negatives(source, negative_words)
# even_negatives('Never', ['never']) → False
# even_negatives('Nothing is not mine.', ['nothing', 'Not']) → True
# even_negatives('notyouneverme', ['never', 'Not', 'no']) → True


def even_negatives(source, negative_words):
    res = {}
    previous_words = []

    for w in negative_words:
        w = w.lower()

        res[w] = source.lower().count(w)

        for i in previous_words:
            res[w] -= i.count(w)

        previous_words.append(w)

    return bool(sum([i for i in res.values()]) % 2 == 0)


print(even_negatives('Never', ['never']))
print(even_negatives('Nothing is not mine.', ['nothing', 'Not']))
print(even_negatives('notyouneverme', ['never', 'Not', 'no']))
