# The task was taken from
# https://www.youtube.com/watch?v=1uIwiIjw1fw
#


def check_if_all_words_available(magazine: str,
                                 ransom_note: str) -> (bool, str):
    magazine_words = {}
    note_words = {}

    for word in magazine.split():
        magazine_words.setdefault(word, 0)
        magazine_words[word] += 1

    for word in ransom_note.split():
        note_words.setdefault(word, 0)
        note_words[word] += 1

    for word, count in note_words.items():
        if word not in magazine_words or count < magazine_words[word]:
            return False, word

    return True


examples = [
    {'magazine': """I was always wonder
     how much my dog loves me in so many ways
     One million of cases that can prove it
     The dog protects my belogings from people
     who want to stole them
     And your dog can get you feeling of the real
     friendship and love without a reason
     """,
     'ransom_note': """Hi I
     stole your dog
     Give me million of dollars
     to get the dog back
     """}
]
for sample in examples:
    result = check_if_all_words_available(**sample)
    print(result)
