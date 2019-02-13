class DynamicArray:

    """ Time Complexity: O(1) """
    def __init__(self):

        self.N = 1
        self.left = self.right = None
        self.xs = self.allocate(1)

    ###########################################################################
    # Utilities
    ###########################################################################

    """ Time Complexity: O(n) """
    def allocate(self, N):
        return [None] * N

    """ Time Complexity: O(n) """
    def resize(self, N):

        xs_ = self.allocate(N)

        for i in range(self.n):
            xs_[i] = self.xs[i]

        self.xs = xs_
        self.N = N

    """ Time Complexity: O(n) """
    def resize_left(self, N):

        xs_ = self.allocate(N)



    """ Time Complexity: O(n) """
    def resize_right(self, N):

        xs_ = self.allocate(N)

        for i in range(self.left, self.right - 1):
            xs_[i] = self.xs[i]

        self.xs = xs_
        self.N = N

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

        if i < 0 or i > self.n - 1:
            raise IndexError()

        return self.xs[i]

    """ Time Complexity: O(1) """
    def set_at(self, i, x):

        if i < 0 or i > self.n - 1:
            raise IndexError()

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
            raise IndexError()

        self.xs[0] = x

    """ Time Complexity: O(1) """
    def set_right(self, x):

        if self.n == 0:
            raise IndexError()

        self.xs[self.n - 1] = x

    ###########################################################################
    # Dynamic sequence operations
    ###########################################################################

    """ Time Complexity: O(n) """
    def insert_at(self, i, x):

        if self.n == self.N:
            self.resize(self.N * 2)

        for j in range(i, self.n):
            self.xs[j + 1] = self.xs[j]

        self.xs[i] = x
        self.n += 1

    """ Time Complexity: O(n) """
    def delete_at(self, i):

        if self.m < self.N // 4:
            self.resize(self.N // 2)

        for j in range(i + 1, self.n):
            self.xs[j - 1] = self.xs[j]

        self.n -= 1

    ###########################################################################
    # Special dynamic sequence operations
    ###########################################################################

    """ Time Complexity: O(n) """
    def insert_left(self, x):
        self.insert_at(0, x)

    """ Time Complexity: O(1) (Amortized) """
    def insert_right(self, x):
        self.insert_at(self.n - 1, x)

    """ Time Complexity: O(n) """
    def delete_left(self):
        self.delete_at(0)

    """ Time Complexity: O(1) (Amortized) """
    def delete_right(self):
        self.delete_at(self.n - 1)
