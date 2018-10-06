"""
Elements in this data structure must have a 'k' property representing a key
for comparisons.
"""
class FixedUnsortedArray:  # noqa: E302

    """ Time Complexity: O(n) """
    def __init__(self, size):

        self.size = size
        self.n = 0
        self.elements = [None] * size

    ###########################################################################
    # Set operations
    ###########################################################################

    """ Time Complexity: O(n) """
    def find(self, k):

        for i in range(self.n):

            if self.elements[i].k == k:
                return self.elements[i]

        return None

    ###########################################################################
    # Dynamic set operations
    ###########################################################################

    """ Time Complexity: O(n) """
    def insert(self, x):

        if self.n == self.size:
            raise IndexError('Insert Error: FixedUnsortedArray is full.')

        self.elements[self.n] = x
        self.n += 1

    """ Time Complexity: O(n) """
    def delete(self, k):

        for i in range(self.n):

            if self.elements[i].k == k:

                for j in range(i, self.n - 1):
                    self.elements[j] = self.elements[j + 1]

                self.n -= 1
                return

        raise KeyError(f'Delete Error: Key {k} is not contained in ' +
                       'FixedUnsortedArray.')

    ###########################################################################
    # Ordered set operations
    ###########################################################################

    """ Time Complexity: O(n) """
    def find_next(self, k):

        next_k = None
        next_element = None

        for i in range(self.n):

            if next_k is None and k < self.elements[i].k:

                next_k = self.elements[i].k
                next_element = self.elements[i]

            elif k < self.elements[i].k < next_k:

                next_k = self.elements[i].k
                next_element = self.elements[i]

        return next_element

    """ Time Complexity: O(n) """
    def find_previous(self, k):

        previous_k = None
        previous_element = None

        for i in range(self.n):

            if previous_k is None and self.elements[i] < k:

                previous_k = self.elements[i].k
                previous_element = self.elements[i]

            elif previous_k < self.elements[i].k < k:

                previous_k = self.elements[i].key
                previous_element = self.elements[i]

        return previous_element

    """ Time Complexity: O(n) """
    def find_max(self):

        if self.n == 0:
            return None

        max_k = self.elements[0].k
        max_element = self.elements[0]

        for i in range(1, self.n):

            if self.elements[i].k > max_k:

                max_k = self.elements[i].k
                max_element = self.elements[i]

        return max_element

    """ Time Complexity: O(n) """
    def find_min(self):

        if self.n == 0:
            return None

        min_k = self.elements[0].k
        min_element = self.elements[0]

        for i in range(1, self.n):

            if self.elements[i].k < min_k:

                min_k = self.elements[i].k
                min_element = self.elements[i]

        return min_element

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
