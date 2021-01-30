# This is my solution for task which was discussed in
# this video: https://www.youtube.com/watch?v=tOD6g7rF7NA
# This task took about 1 hour to solve.

# Our string is first 31 numbers of Pi
my_string = '3141592653589793238462643383279'
my_patterns = ['314', '49', '15926535897', '14', '9323',
               '8462643383279', '4', '793']


def get(s, patterns):
    # Sort patterns in descendent order, we need to check
    # the longest substrings first to find the solution
    # with smallest number of whitespaces in result
    patterns = sorted(patterns, key=len)[::-1]

    for i, p in enumerate(patterns):
        pos = s.find(p)

        if pos >= 0:
            # Remove the substring from string to make sure that different
            # substrings will not be intersected
            s = ' '.join(s.split(p, 1))
            ind = i  # remember the position of a pattern in array
                     # to check other patterns that have less length

            while ind < len(patterns) - 1:
                collected = [(pos, p)]  # remember the substring and it's global position
                ind += 1

                for p2 in patterns[ind:]:
                    pos2 = s.find(p2)

                    if pos2 >= 0:
                        s = ' '.join(s.split(p2, 1))
                        collected.append((pos2, p2))

                # Check if string still have any numbers, if string
                # contains only white spaces - it means we found
                # the best solution
                if s.replace(' ', '') == '':
                    res = ' '.join([s[1] for s in sorted(collected)])
                    return res


result = get(my_string, my_patterns)
print(result.count(' '), result)
