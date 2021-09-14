from random import randint


class PriorityHeap:

    def __init__(self):
        self.heap = []

    def _switch(self, node_1, node_2):
        """ Меняем элементы местами. """

        tmp = self.heap[node_1]
        self.heap[node_1] = self.heap[node_2]
        self.heap[node_2] = tmp

    def get_parent(self, node_id):
        """ Получаем индекс родительской ноды. """

        return node_id // 2

    def get_left_child(self, node_id):
        """ Получаем индекс левой дочерней ноды. """

        child_id = node_id * 2 + 1
        if child_id < self.size():
            return child_id

    def get_right_child(self, node_id):
        """ Получаем индекс правой дочерней ноды. """

        child_id = node_id * 2 + 2
        if child_id < self.size():
            return child_id

    def size(self):
        """ Получаем длину кучи. """

        return len(self.heap)

    def _go_up(self, position):
        """ Поднимаем элемент вверх по куче, пока порядок
            не будет восстановлен.
        """

        parent = self.get_parent(position)

        while self.heap[parent] < self.heap[position]:
            self._switch(parent, position)
            position = parent
            parent = self.get_parent(position)

    def _go_down(self, element):
        """ Спускаем элемент вниз по куче, пока порядок не
            будет восстановлен.
        """

        left_child = self.get_left_child(element)
        right_child = self.get_right_child(element)

        # choose what child is better
        max_child = left_child
        if left_child:
            if right_child:
                if self.heap[right_child] > self.heap[left_child]:
                    max_child = right_child

        if max_child and self.heap[max_child] > element:
            self._switch(element, max_child)
            self._go_down(max_child)

    def pop(self):
        """ Забираем максимальный элемент из кучи.

            Забираем максмальный элемент из кучи, на его место ставим
            последний элемент и опускаем этот элемент вниз по куче.
        """

        if self.size():
            res = self.heap[0]
            self.heap[0] = self.heap[-1]
            del self.heap[-1]

            self._go_down(0)

            return res

    def insert(self, item):
        """ Вставка элемента в стэк.

            Вставляем элемент в конец спска и поднимаем его вверх по куче.
        """

        self.heap.append(item)

        position = self.size() - 1
        self._go_up(position)

    def get_max_items(self, elements_count = 1):
        """ Возвращает список N максмальных элементов из кучи. """

        return [self.pop() for i in range(elements_count)]


my_heap = PriorityHeap()

for i in range(20):
    my_heap.insert(randint(1, 100))

print(f'Heap: {my_heap.heap}')

top_elements = my_heap.get_max_items(5)
print(f'Top 5 elements: {top_elements}')
