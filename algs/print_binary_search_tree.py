

# __10__
#  / \
# 8  15


class Node(object):
    value = None
    left_node = None
    right_node = None

    def __init__(self, value):
        self.value = value

    def print(self, size, new_line=True):
        s = '_' * (size-1) + " {0} " + '_' * (size-1)

        if new_line:
            s += '\n'
        if self.left_node:
            s = s + ' /'
        else:
            s += ' ' * 2 * size

        if self.right_node:
            s = s + ' ' * size + ' \\'
        if new_line:
            s += '\n'

        print(s.format(self.value), end='')
        if self.left_node:
            self.left_node.print(1, False)
        else:
            s += '_' * (size-1)
        if self.right_node:
            self.right_node.print(size-1)
        else:
            s += '_' * (size-1)

    def insert(self, value):
        if not self.value:
            self.value = value

        elif value < self.value:
            if not self.left_node:
                self.left_node = Node(value)
            else:
                self.left_node.insert(value)

        elif value >= self.value:
            if not self.right_node:
                self.right_node = Node(value)
            else:
                self.right_node.insert(value)


class BinaryTree(object):
    root = None
    size = 0

    def insert(self, value):
        self.size += 1
        if not self.root:
            self.root = Node(value)
        else:
            self.root.insert(value)

    def print(self):
        self.root.print(self.size)


b_tree = BinaryTree()
b_tree.insert(5)
b_tree.insert(10)
b_tree.insert(11)
b_tree.insert(1)
b_tree.print()
