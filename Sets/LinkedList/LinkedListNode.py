class LinkedListNode:

    """ Time Complexity: O(1) """
    def __init__(self, left=None, x=None, right=None):

        self.left = left
        self.x = x
        self.right = right

    """ Time Complexity: O(1) """
    def get_left(self):
        return self.left

    """ Time Complexity: O(1) """
    def set_left(self, left):
        self.left = left

    """ Time Complexity: O(1) """
    def get_x(self):
        return self.x

    """ Time Complexity: O(1) """
    def set_x(self, x):
        self.x = x

    """ Time Complexity: O(1) """
    def get_right(self):
        return self.right

    """ Time Complexity: O(1) """
    def set_right(self, right):
        self.right = right
