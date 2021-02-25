# Here we are creating the linked list and then we
# will create another linked list which will be reversed
# linked list.


class Element(object):
    next = None

    def __init__(self, value):
        self.value = value


class LinkedList(object):
    head = None
    last = None
    my_length = 0

    def __init__(self, values=None):
        values = values or []

        for v in values:
            self.add(v)

    def add(self, value):
        """ Add new element to the end of linked list. """

        my_element = Element(value)

        if self.last:
            self.last.next = my_element

        self.last = my_element
        self.head = self.head or my_element
        self.my_length += 1

    def pop(self):
        """ Extract the first element from linked list. """

        res = self.head

        if res:
            self.head = res.next

            self.my_length -= 1

            return res.value
        else:
            raise IndexError('pop from empty list')

    def __len__(self):
        """ Get the length of the whole linked list. """

        return self.my_length


def reverse_linked_list1(list_to_reverse):
    """ This function reverse the linked list by getting
        the whole array of the elements and the putting
        these elements to the next LinkedList in the opposite
        order.
    """

    my_new_list = LinkedList()
    all_elements = []

    while len(list_to_reverse) > 0:
        element = list_to_reverse.pop()
        all_elements.append(element)

    for e in all_elements[::-1]:
        my_new_list.add(e)

    return my_new_list


def reverse_linked_list2(my_list):
    """ This function reverts linked list
        rewriting the links between the elements
        in the opposite direction.
    """

    previous_element = None
    element = my_list.head

    while element:
        next_element = element.next
        element.next = previous_element
        previous_element = element
        element = next_element
        my_list.head = previous_element


# Create linked list:
my_list = LinkedList([1, 2, 50, 607])
# Add new element to the end of the list
my_list.add(3)

# Extract first two elements from the linked list:
print('Extract first element:', my_list.pop())
print('Extract second element:', my_list.pop())

# Get the length of the list:
print('Length of linked list', len(my_list))

# Get reversed linked list using the first approach
print('Reversing...')
new_list = reverse_linked_list1(my_list)

print('* ' * 20)
# Extract first two elements from the linked list:
print('Extract first element:', new_list.pop())
print('Extract second element:', new_list.pop())

# Create new Linked List
my_list = LinkedList([1, 5, 100])

print('/ ' * 20)
# Reverse linked list using the second approach
reverse_linked_list2(my_list)
print('/ ' * 20)

# Extract first two elements of linked list:
print('Extract first element:', my_list.pop())
print('Extract second element:', my_list.pop())
