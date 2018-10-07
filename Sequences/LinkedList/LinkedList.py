import LinkedListNode


class LinkedList:

    """ Time Complexity: O(1) """
    def __init__(self):

        self.n = 0
        self.left = self.right = None

    ###########################################################################
    # Sequence operations
    ###########################################################################

    """ Time Complexity: O(1) """
    def len(self):
        return self.n

    """ Time Complexity: O(n) """
    def seq_iter(self):

        node = self.left
        while node:

            print(str(node.get_x()) + ' ')

            node = node.get_right()

    """ Time Complexity: O(n) """
    def at(self, i):

        j = 0
        node = self.left
        while node:

            if j == i:
                return node.get_x()

            j += 1
            node = node.get_right()

    """ Time Complexity: O(n) """
    def set_at(self, i, x):

        j = 0
        node = self.left
        while node:

            if j == i:
                node.set_x(x)

            j += 1
            node = node.get_right()

    ###########################################################################
    # Special sequence operations
    ###########################################################################

    """ Time Complexity: O(1) """
    def left(self):

        if not self.left:
            return None

        return self.left.get_x()

    """ Time Complexity: O(1) """
    def right(self):

        if not self.right:
            return None

        return self.right.get_x()

    """ Time Complexity: O(1) """
    def set_left(self, x):

        if not self.left:
            return

        self.left.set_x(x)

    """ Time Complexity: O(1) """
    def set_right(self, x):

        if not self.right:
            return

        self.right.set_x(x)

    ###########################################################################
    # Dynamic sequence operations
    ###########################################################################

    """ Time Complexity: O(n) """
    def insert_at(self, i, x):

        if i == 0:
            self.insert_left(x)
        elif i == self.n - 1:
            self.insert_right(x)
        else:

            j = 0
            node = self.left
            while node:

                if j == i:

                    x_node = LinkedListNode(node.get_left(), x, node)
                    node.get_left().set_right(x_node)
                    node.set_left(x_node)

                    return

                j += 1
                node = node.get_right()

    """ Time Complexity: O(n) """
    def delete_at(self, i):

        if i == 0:
            self.delete_left()
        elif i == self.n - 1:
            self.delete_right()
        else:

            j = 0
            node = self.left
            while node:

                if j == i:

                    node.get_left().set_right(node.get_right())
                    node.get_right().set_left(node.get_left())
                    return

                j += 1
                node = node.get_right()

    ###########################################################################
    # Special dynamic sequence operations
    ###########################################################################

    """ Time Complexity: O(1) """
    def insert_left(self, x):

        x_node = LinkedListNode(None, x, self.left)

        if not self.left and not self.right:
            self.left = self.right = x_node
        else:
            self.left.set_left(x_node)

        self.left = x_node

    """ Time Complexity: O(1) """
    def insert_right(self, x):

        x_node = LinkedListNode(self.right, x, None)

        if not self.left and not self.right:
            self.left = self.right = x_node
        else:
            self.right.set_right(x_node)

        self.right = x_node

    """ Time Complexity: O(1) """
    def delete_left(self):

        if not self.left and not self.right:
            return
        elif self.left == self.right:
            self.left = self.right = None
        else:

            self.left.get_right().set_left(None)
            self.left = self.left.get_right()

    """ Time Complexity: O(1) """
    def delete_right(self):

        if not self.left and not self.right:
            return
        elif self.left == self.right:
            self.left = self.right = None
        else:

            self.right.get_left().set_right(None)
            self.right = self.right.get_left()
