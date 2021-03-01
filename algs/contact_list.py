# The task was taken from
# https://www.youtube.com/watch?v=vlYZb68kAY0
#

from treelib import Tree
from treelib import Node as PrintNode

# Examples:
# Alice 777
# Alexander 2121
# Bob   545


class Node(object):
    value = None
    phone = ''
    child_nodes = None

    def __init__(self, value):
        self.value = value
        self.child_nodes = []

    def get_child(self, value):
        for node in self.child_nodes:
            if node.value == value:
                return node

    def add_node(self, value):
        new_node = Node(value)
        self.child_nodes.append(new_node)
        return new_node

    def print(self, n_tabs=1):
        print('|'*n_tabs, self.value)

        for child in self.child_nodes:
            child.print()

    def count_of_contacts(self):
        result = 0
        if self.phone:
            result += 1

        if not self.child_nodes:
            return result

        for child in self.child_nodes:
            result += child.count_of_contacts()

        return result


class Contacts(object):
    my_tree = Node('*')

    def add(self, name, phone):
        parent = self.my_tree

        for char in name:
            child = parent.get_child(char)
            if child:
                parent = child
            else:
                parent = parent.add_node(char)

        parent.phone = phone

    def search(self, name):
        root = self.my_tree
        result = 0
        for char in name:
            node = root.get_child(char)

            if not node:
                return 0
            else:
                if node.phone:
                    result += 1
                root = node

        return result + root.count_of_contacts()


contacts = Contacts()
contacts.add('test', '333')
contacts.add('timur', '343')
contacts.add('test call', '33444')


examples = ['t', 'te', 'ti', 'z']
for sample in examples:
    res = contacts.search(sample)
    print('{0} -> {1}'.format(sample, res))
