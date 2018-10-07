class FixedUnsortedArray:

    """ Time Complexity: O(1) """
    def __init__(self):

        self.n = 0
        self.xs = None

    ###########################################################################
    # Utilities
    ###########################################################################

    """ Time Complexity: O(n) """
    def allocate(self, N):
        return [None] * N

    ###########################################################################
    # Set operations
    ###########################################################################

    """ Time Complexity: O(n) """
    def find(self, k):

        for i in range(self.n):

            if self.xs[i].k == k:
                return self.xs[i]

        return None

    """ Time Complexity: O(n) """
    def iter(self):

        for i in range(self.n):
            print(str(self.xs[i]) + ' ')

    ###########################################################################
    # Dynamic set operations
    ###########################################################################

    """ Time Complexity: O(n) """
    def insert(self, x):

        xs_ = self.allocate(self.n + 1)

        for i in range(self.n):
            xs_[i] = self.xs[i]

        xs_[self.n] = x

        self.xs = xs_
        self.n += 1

    """ Time Complexity: O(n) """
    def delete(self, k):

        xs_ = self.allocate(self.n - 1)

        for i in range(self.n):

            if self.xs[i].k == k:

                for j in range(i, self.n - 1):
                    xs_[j] = self.xs[j + 1]

                self.xs = xs_
                self.n -= 1
                return

            if i == self.n - 1:
                return

            xs_[i] = self.xs[i]

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

        for i in range(self.n):

            if (k < self.xs[i].k < next_k) \
               or (next_k is None and k < self.xs[i].k):

                next_k = self.xs[i].k
                next_x = self.xs[i]

        return next_x

    """ Time Complexity: O(n) """
    def find_previous(self, k):

        previous_k = None
        previous_x = None

        for i in range(self.n):

            if (previous_k < self.xs[i].k < k) \
               or (previous_k is None and self.xs[i] < k):

                previous_k = self.xs[i].k
                previous_x = self.xs[i]

        return previous_x

    """ Time Complexity: O(n) """
    def find_max(self):

        if self.n == 0:
            return None

        max_k = self.xs[0].k
        max_x = self.xs[0]

        for i in range(1, self.n):

            if self.xs[i].k > max_k:

                max_k = self.xs[i].k
                max_x = self.xs[i]

        return max_x

    """ Time Complexity: O(n) """
    def find_min(self):

        if self.n == 0:
            return None

        min_k = self.xs[0].k
        min_x = self.xs[0]

        for i in range(1, self.n):

            if self.xs[i].k < min_k:

                min_k = self.xs[i].k
                min_x = self.xs[i]

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
