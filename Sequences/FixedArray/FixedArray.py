class FixedArray:

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
    # Sequence operations
    ###########################################################################

    """ Time Complexity: O(1) """
    def len(self):
        return self.n

    """ Time Complexity: O(n) """
    def seq_iter(self):

        for i in range(self.n):
            print(str(self.xs[i]) + ' ')

    """ Time Complexity: O(1) """
    def at(self, i):
        return self.xs[i]

    """ Time Complexity: O(1) """
    def set_at(self, i, x):
        self.xs[i] = x

    ###########################################################################
    # Special sequence operations
    ###########################################################################

    """ Time Complexity: O(1) """
    def left(self):

        if self.n == 0:
            return None

        return self.xs[0]

    """ Time Complexity: O(1) """
    def right(self):

        if self.n == 0:
            return None

        return self.xs[self.n - 1]

    """ Time Complexity: O(1) """
    def set_left(self, x):

        if self.n == 0:
            return

        self.xs[0] = x

    """ Time Complexity: O(1) """
    def set_right(self, x):

        if self.n == 0:
            return

        self.xs[self.n - 1] = x

    ###########################################################################
    # Dynamic sequence operations
    ###########################################################################

    """ Time Complexity: O(n) """
    def insert_at(self, i, x):

        xs_ = self.allocate(self.n + 1)

        for j in range(i):
            xs_[j] = self.xs[j]

        xs_[i] = x

        for j in range(i, self.n):
            xs_[j + 1] = self.xs[j]

        self.xs = xs_
        self.n += 1

    """ Time Complexity: O(n) """
    def delete_at(self, i):

        xs_ = self.allocate(self.n - 1)

        for j in range(i):
            xs_[j] = self.xs[j]

        for j in range(i + 1, self.n):
            xs_[j - 1] = self.xs[j]

        self.xs = xs_
        self.n -= 1

    ###########################################################################
    # Special dynamic sequence operations
    ###########################################################################

    """ Time Complexity: O(n) """
    def insert_left(self, x):
        self.insert_at(0, x)

    """ Time Complexity: O(n) """
    def insert_right(self, x):
        self.insert_at(self.n - 1, x)

    """ Time Complexity: O(n) """
    def delete_left(self):
        self.delete_at(0)

    """ Time Complexity: O(n) """
    def delete_right(self):
        self.delete_at(self.n - 1)
