import LinkedListNode


class LinkedList:

    """ Time Complexity: O(1) """
    def __init__(self):
        self.head = None

    ###########################################################################
    # Set operations
    ###########################################################################

    """ Time Complexity: O(n) """
    def find(self, k):

        node = self.head
        while node is not None:

            if node.get_x().k == k:
                return node.get_x()

            node = node.get_right()

        return None

    ###########################################################################
    # Dynamic set operations
    ###########################################################################

    """ Time Complexity: O(1) """
    def insert(self, x):

        node = LinkedListNode(None, x, self.head)
        self.head.set_left(node)
        self.head = node

    """ Time Complexity: O(n) """
    def delete(self, k):

        node = self.head
        while node is not None:

            if node.get_x().k == k:

                node.get_left().set_right(node.get_right())
                return

            node = node.get_right()

        raise KeyError(f'Delete Error: Key {k} is not contained in ' +
                       'LinkedList.')

    ###########################################################################
    # Ordered set operations
    ###########################################################################

    """ Time Complexity: O(n) """
    def find_next(self, k):

        next_k = None
        next_x = None

        node = self.head
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

        node = self.head
        while node is not None:

            if (previous_k < node.get_x().k < k) \
               or (previous_k is None and node.get_x().k < k):

                previous_k = node.get_x().k
                previous_x = node.get_x()

            node = node.get_right()

        return previous_x

    """ Time Complexity: O(n) """
    def find_max(self):

        if self.head is None:
            return None

        max_k = self.head.get_x().k
        max_x = self.head.get_x()

        node = self.head
        while node is not None:

            if node.get_x().k > max_k:

                max_k = node.get_x().k
                max_x = node.get_x()

            node = node.get_right()

        return max_x

    """ Time Complexity: O(n) """
    def find_min(self):

        if self.head is None:
            return None

        min_k = self.head.get_x().k
        min_x = self.head.get_x()

        node = self.head
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
