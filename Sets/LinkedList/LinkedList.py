import LinkedListNode


class LinkedList:

    """ Time Complexity: O(1) """
    def __init__(self):

        self.n = 0
        self.left = self.right = None

    ###########################################################################
    # Set operations
    ###########################################################################

    """ Time Complexity: O(n) """
    def find(self, k):

        node = self.left
        while node is not None:

            if node.get_x().k == k:
                return node.get_x()

            node = node.get_right()

        return None

    """ Time Complexity: O(n) """
    def iter(self):

        node = self.left
        while node is not None:

            print(str(node.get_x()) + ' ')

            node = node.get_right()

    ###########################################################################
    # Dynamic set operations
    ###########################################################################

    """ Time Complexity: O(1) """
    def insert(self, x):

        if self.n == 0:
            self.left = self.right = LinkedListNode(None, x, None)

        elif self.n > 0:

            x_node = LinkedListNode(None, x, None)
            x_node.set_right(self.left)
            self.left.set_left(x_node)
            self.left = x_node

            self.n += 1

    """ Time Complexity: O(n) """
    def delete(self, k):

        i = 0
        node = self.left
        while node is not None:

            if node.get_x().k == k:

                if self.n == 1:

                    self.left = self.right = None
                    self.n -= 1

                    return

                elif i == 0:

                    self.left = self.left.get_right()
                    self.left.set_right(None)

                    self.n -= 1
                    return

                elif i == self.n - 1:

                    self.right = self.right.get_left()
                    self.right.set_right(None)

                    self.n -= 1
                    return

                elif 0 < i < self.n - 1:

                    node.get_right().set_left(node.get_left())
                    node.get_left().set_right(node.get_right())

                    self.n -= 1
                    return

            i += 1
            node = node.get_right()

    ###########################################################################
    # Ordered set operations
    ###########################################################################

    """ Time Complexity: O(n) """
    def order_iter(self):
        pass

    """ Time Complexity: O(n) """
    def find_next(self, k):

        next_k = None
        next_x = None

        node = self.left
        while node is not None:

            if (k < node.get_x().k < next_k) \
               or (next_k is None and k < node.get_x().k):

                next_k = node.get_x().k
                next_x = node.get_x()

            node = node.get_right()

        return next_x

    """ Time Complexity: O(n) """
    def find_previous(self, k):

        previous_k = None
        previous_x = None

        node = self.left
        while node is not None:

            if (previous_k < node.get_x().k < k) \
               or (previous_k is None and node.get_x().k < k):

                previous_k = node.get_x().k
                previous_x = node.get_x()

            node = node.get_right()

        return previous_x

    """ Time Complexity: O(n) """
    def find_max(self):

        if self.left is None:
            return None

        max_k = self.left.get_x().k
        max_x = self.left.get_x()

        node = self.left
        while node is not None:

            if node.get_x().k > max_k:

                max_k = node.get_x().k
                max_x = node.get_x()

            node = node.get_right()

        return max_x

    """ Time Complexity: O(n) """
    def find_min(self):

        if self.left is None:
            return None

        min_k = self.left.get_x().k
        min_x = self.left.get_x()

        node = self.left
        while node is not None:

            if node.get_x().k < min_k:

                min_k = node.get_x().k
                min_x = node.get_x()

            node = node.get_right()

        return min_x

    ###########################################################################
    # Dynamic ordered set operations
    ###########################################################################

    """ Time Complexity: O(n) """
    def delete_max(self):

        max_k = self.find_max()

        if max_k is not None:
            self.delete(max_k)

    """ Time Complexity: O(n) """
    def delete_min(self):

        min_k = self.find_min()

        if min_k is not None:
            self.delete(min_k)
