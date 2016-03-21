#!/usr/bin/env python
from __future__ import print_function

# Now that you've used things like lists and dictionaries in Python, i.e.,
# "collections" or "containers" of "objects", I want to get more fundamental
# for a second. Let's think about what, for example, a list really "is".

# Thought Experiment (spend a few minutes before moving on): If you wanted to
# create a list in Python, you would just write something like, "l = []", and
# then start to append items or extend the list, etc. But, what if you were
# asked to make a list and not use the brackets (i.e., don't use Python's
# built-in list type or any other container for objects that Python provides,
# such as dictionaries, etc.)? Think about how you might try to represent
# the idea of a list if you couldn't actually make a Python list. A really
# naive way of doing it would be to make variables to store each value, i.e.,
#
#  first = 5
#  second = 4
#  third = 5
#
# But you see the issue here. There's no actual collection of objects and
# there's no ordering or relation between the objects. So, how might you
# represent this information?

# Linked Lists
# A key building block in computer science is the concept of a linked list,
# i.e., a collection of objects whose elements are linked together so as to
# form a representation of a list. For example, consider the situation above
# where we had defined "first", "second", and "third" variables. Imagine that
# each of these variables actually stored not only a value, but also a "link",
# i.e., "first" would store a link to "second", "second" would store a link to
# "third", and "third" would store a link whose value was None (since it's the
# last element). This is the basic idea behind a linked list. This assignment
# will be about making a linked list implementation and using it rather than
# Python's own list implementation (which is much better and faster) but is
# built utimately using the same kind of implementation at some deep level.

# What we need first is to create a custom type of "object" that will
# represent a "node" in the list. Let's call it "Node". This object will have
# a couple attributes that can be changed: a "value" attribute (which will
# store the value of list element, i.e., 5.8 or 19 or "the") and a "next_node"
# attribute, which will store a reference to the next node (if one exists).
# Below I will define a class for use in this assignment just to start it off.
# the "__init__" method is a required method (not technically, but for our
# purposes, let's just say it is) that you have to define for a Python class.
# It gets called when an object of type `Node` is instantiated. A `value` for
# the node and a reference to the following node can be passed in, but both are
# technically optional (when you want to give a default value to a parameter,
# you can specify the default value via `value=None`, for example, in the
# function signature). What would happen if I just created an object of type
# `Node` via "a = Node()"? What would `a`'s `value` attribute be equal to
# (i.e., `a.value`)? And what would `a.next_node` be equal to? Both would be
# equal to None since I did not specify a value for either parameter. With this
# implementation of `Node`, I could execute the following:
#
#  third = Node(value=7.2, next_node=None)
#  second = Node(value=6.7, next_node=third)
#  first = Node(value=1.0, next_node=second)
#
# This gives us a basic "linked list". As long as I have a reference to the
# first element, I can traverse the list to get to the other elements. For
# example:
#
#  i = 0
#  current_node = first
#  while True:                                # keep on iterating until breaking
#
#      print("Node {}: {}".format(current_node.value)) # print `node`'s value
#
#      if current_node.next_node is None:     # check if current node is the last
#                                             # node
#          break
#      current_node = current_node.next_node  # update `current_node`
#
#      i += 1                                 # increment i
#
# This would print out the following:
#
#  Node 0: 1.0
#  Node 1: 6.7
#  Node 2: 7.2
#
class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

# Now that we have a class to represent each node in the linked list, there are
# just a couple other points to mention before implementing the actual linked
# list class. Firstly, it is customary to implement a sort of "header" node,
# which can be understood as a node that does not have a value and whose only
# function is to point to the first node. When passing around a reference to
# a linked list, it will be necessary to figure out where to start. Next, the
# implementation of `LinkedList` will have to contain many of the methods for
# doing things like adding elements to the list, deleting them, etc., that
# make it useful as a data structure. The main part of this assignment will be
# to extend the `LinkedList` class below to add functionality to it and then to
# use this functionality in a real program. I will start off the implementation
# by making the __init__ method and a couple other methods and then I will add
# so-called stub methods (unimplemented methods) that you will have to fill
# out.
#
# Notes
#
#  1. In Python classes, most methods/functions will take a first argument
#     called `self`. Notice how, when I wanted to make a `Node` object, for
#     example, I did not need to specify `self` even though it shows up in the
#     method signature, "def __init__(self, value=None, next_node=None)". I
#     could make a new node just by executing "Node(value=3.4)" or even just
#     "Node()". The `self` argument refers to the instantiation of the class
#     itself. That's why in the method you see things like "self.value =
#     value". This is setting the object's `value` attribute to the value of
#     the passed-in parameter (also named) `value`. Don't think too much about
#     what `self` is. Just use it as you see it used here. But do NOT forget
#     it. Things will break if it's not included.
#  2. The text included inside the three double quotation marks

class LinkedList:
    """
    Python implementation of a linked list.
    """

    def __init__(self):
        """
        Initialize an empty linked list (other than a header node that
        points to nothing).
        """

        self.header_node = Node()

    def is_empty(self):
        """
        Return False if the list contains any elements or True if not.

        :returns: boolean value
        :rtype: bool
        """

        # Check if the object's `header_node` attribute actually points
        # to a node or if its `next_node` value is None
        if self.header_node.next_node is None:
            return True
        return False

    def add_to_beginning(self, new_value):
        """
        Add new node with the given value to the start of the list.

        :param new_value: new value to add to the beginning of the list
        :type new_value: object
        """

        # Create a new Node and set its `value` attribute to the given
        # value and set its `next_node` attribute to the value of the
        # current first node in the list
        new_node = Node(value=new_value, next_node=header_node.next_node)

        # Now, set the value of `header_node`'s `next_node` attribute to
        # point to this new node
        self.header_node.next_node = new_node


    def append(self, new_value):
        """
        Append new value to the end of the linked list.
        
        :param new_value: new value to append to list (inside a node)
        :type new_value: object (basically, this means any type)
        """

        # Start at the beginning of the linked list, which can be
        # reached via the object's `header_node` attribute
        current_node = header_node
        while True:

            # Check if this node happens to be the last node in the
            # list, in which case we have found the location we need to
            # modify
            # Note: This would even work for an empty linked list since
            # value of `header_node`'s `next_node` attribute is None
            # until it's changed by adding nodes to the list (i.e., by
            # using this method, for example).
            if current_node.next_node is None:

                # Make a new node with the given value and set
                # `current_node`'s `next_node` attribute to point to
                # this new node we're creating (which will be
                # initialized to have a `value`, but will have a
                # `next_node` value that gets the default value, i.e.,
                # None)
                current_node.next_node = Node(value=new_value)

                # Break out of loop
                break

    def find_index_of_value(self, value_to_find):
        """
        Find the index of the first occurrence of the given value in the
        list. If it is not found, return -1 to signify that the value
        was not found.

        :param value_to_find: value to look for in the elements of the
                              linked list
        :type value_to_find: object

        :returns: index of the first element matching the given value
                  (or -1 if the value was not found in the list at all)
        :rtype: int
        """

        # Let's first check to see if the list is empty by calling the
        # object's `is_empty` function, which simply looks to see if the
        # object's `header_node` attribute's `value` attribute is equal
        # to None
        if self.is_empty():
            return -1

        # If the list is not empty, let's start at the first real node,
        # i.e., the node that is pointed to by the object's
        # `header_node`'s `next_node` attribute
        current_node = self.header_node.next_node

        # Loop through the elements of the list and keep a counter for
        # the index
        index = 0
        while True:
            
            # If the value of the current node is equal to the value
            # we're trying to find, then return the value of `index`
            # since we're finished
            if current_node.value == value_to_find:
                return index

            # Otherwise, check if this is the last node and, if so,
            # return -1 since that means the value was nowhere to be
            # found
            if current_node.next_node is None:
                return -1

            # Move forward one node and increment the counter
            # Note: Notice that I am not using an `else` statement here
            # (or even above after the second `if` block). Why/how can I
            # do this? The reason is that the `if` condition, if met,
            # would lead to a situation where the code below it would
            # never be executed. Thus, logically, there is no need to
            # put an `else` statement. This is naturally an `else`
            # statement.
            current_node = current_node.next_node
            index += 1

    # Note: Python includes something called "magic" methods. They are
    # a set of predefined method/function names that allow objects to
    # be used in certain very useful ways if they are implemented. For
    # example, `__len__` is one of these so-called magic functions. If
    # you create a custom class (as we are doing here), implementing a
    # `__len__` function will mean that we will be able to call `len` on
    # an object of type `LinkedList`. For example, consider the code
    # below:
    #
    #  x = LinkedList()
    #  x.add_to_beginning(5)
    #  x.add_to_beginning(6)
    #  print(len(x))
    #
    # The call to `print` will print out the length of `x` (should be
    # 2). You might ask how `len` can be called since what actually was
    # implemented was called `__len__`, but just know that this is the
    # magic part. In Python, the `len` function can be used on many
    # different types of objects (actually, any object for which
    # `__len__` is implemented). It's nice to be able to print out the
    # length of a list or the number of elements in a set or the number
    # of keys in a dictionary, etc. But, we could implement `__len__` to
    # do something weird, like return the value 67 no matter what. This
    # would be kind of dumb, but it would be possible. The point is just
    # to demonstrate this capability in Python. Other magic methods
    # include `__add__` (which allow objects to be added together via
    # the `+` operator), `__sub__` (same thing, but with `-`),
    # `__mult__` (same thing, but with `*`), etc. Below I want you to
    # implement the `__len__` function. Simply count the number of
    # elements by iterating until you get to the end and return that
    # number. I am going to implement another magic method here called
    # `__str__`, which allows you to specify the way the object should
    # be "printed", i.e., how you want to represent it. Let's use
    # double braces to distinguish objects of type LinkedList from
    # objects that are just regular Python lists.
    def __len__(self):
        """
        Return the number of elements that are in the list (not
        including the header node that does not contain an element).
        
        :returns: number of elements in list
        :rtype: int
        """

        ### IMPLEMENT THIS METHOD
        # Hint: Check if list is empty. If so, return 0. Otherwise, make
        # a counter and iterate over the list's elements until you get
        # to the element whose `next_node` value is equal to None (i.e.,
        # the last element).

    def __str__(self):
        """
        Return a string representation of the linked list object.

        :returns: string representation of the linked list object
        :rtype: str
        """

        str_repr = None

        # Add string representations of the linked list's values
        # themselves to the string representation of the linked list
        if not self.is_empty():
            current_node = self.header_node.next_node
            while True:

                # Concatenate the string value of the current node's
                # value to the string representation of the linked list
                # object
                if str_repr:
                    str_repr = ", ".join([str_repr, current_node.value])
                else:
                    str_repr = str(current_node.value)
                
                # Break if the current node is the last node
                if current_node.next_node is None:
                    break
                
                # Move forward to next node
                current_node = current_node.next_node

        return str_repr

    def remove_value(self, value_to_delete):
        """
        Find and remove first occurrence of the given value and return
        True if the removal was successful or False if the value could
        not be located anywhere in the list.

        :param value_to_delete: value to find/remove in the list
        :tyep value_to_delete: object

        :returns: whether or not the value was found/removed
        :rtype: bool
        """

        ### IMPLEMENT THIS FUNCTION
        # Hint: Use `find_index_of_value` to figure out whether the
        # given value is even in the list. (You may also want to first
        # use `is_empty`, which, if it returns True, would tell you
        # that the return value is obviously False since there are no
        # possible values to remove.) Once you have the index of the
        # value to remove, iterate through the list's elements and stop
        # at the index of the element preceding the index that you
        # found. Store a reference to this node (as, say, `prev_node`).
        # Then, store a reference to the next node's `next_node` value
        # (i.e., to get the thing that that node is pointing to). If
        # using the `prev_node` notation, you could refer to the next
        # node's `next_node` value via `prev_node.next_node.next_node`,
        # for example. It's possible that the thing that that next node
        # points to is the value None, which would mean that the value
        # you are removing is simply the last value in the list. This
        # doesn't really change anything, though. Now, all you need to
        # do is set the value of `prev_node`'s `next_node` value to the
        # value of `prev_node.next_node`'s `next_node` value, i.e.,
        # skipping over a whole node. You don't need to do anything
        # else. Removing the reference to a node is the same as deleting
        # it (i.e., Python will take care of actually deleting it and
        # freeing up the memory).

    def subsequence(self, i, j):
        """
        Return a new `LinkedList` object that consists of the elements
        in the object's linked list that are at indices `i` up to (but
        not    including) `j`. If `j` represents a value that is larger
        than the length of the linked list, just include the rest of the
        list.

        :param i: start index
        :type i: int
        :param j: stop index
        :type j: int

        :returns: new linked list consisting of a subsequence of the
                  elements in the current linked list
        :rtype: LinkedList

        :raises IndexError: if `i` is too large
        :raises ValueError: if the linked list is emtpy or if `i`/`j`
                            are invalid values or `i` is larger than `j`
        """

        # IMPLEMENT THIS FUNCTION
        # THIS IS PROBABLY GOING TO BE PRETTY HARD. IT'S EXTRA CREDIT.
        # I will start you off by implementing the part that determines
        # whether or not this can actually be done given the value of
        # `i` (i.e., if `i` is an index that does not even occur in the
        # list) and the part that checks the length of the proposed
        # subsequence to see if it's zero, in which case an empty
        # `LinkedList` will be returned, etc.

        # Check parameter values and make sure they make sense
        if any(isinstance(x, int) for x in [i, j]):
            raise ValueError("Parameters i and j should be integer vaues.")

        # Check if `i` is larger than `j`
        if i > j:
            raise ValueError("Parameter i is larger than parameter j.")

        # Check if list is empty
        if self.is_empty():
            raise ValueError("Linked list is currently empty!")

        # Make sure there are enough elements in the list given the
        # value of `i`
        if len(self) - 1 <= i:
            raise IndexError("The value of i is too large. The linked list "
                             "only contains {} elements.".format(len(self)))

        # Check if the length of the subsequence is zero
        if i == j:
            return LinkedList()

        # Ok, now you will do the rest. Basically, you're going to need
        # make a new `LinkedList` here and append each element starting
        # at index `i` in the current linked list and ending right
        # before index `j` (or ending when the linked list ends,
        # whichever comes first).

    def pop_from_beginning(self):
        """
        Remove and return the value of the first node (after the header
        node).

        :returns: value of first node
        :rtype: object
        """

        ### IMPLEMENT THIS
        # Hint: If there is at least one element to pop off the list,
        # get the value of `header_node.next_node.value` and store it in
        # a variable and then set `header_node.next_node` to
        # `header_node.next_node.next_node`. Then, return the value that
        # you stored in a variable.

    def pop_from_end(self):
        """
        Remove and return the value of the first node (after the header
        node).

        :returns: value of first node
        :rtype: object
        """

        ### IMPLEMENT THIS
        # Hint: If there is at least one element to pop off the list,
        # get the value of `header_node.next_node.value` and store it in
        # a variable and then set `header_node.next_node` to
        # `header_node.next_node.next_node`. Then, return the value that
        # you stored in a variable.


def main():

    # Let's make a linked list using our implementation
    linked_list_1 = LinkedList()

    # Let's append elements to it
    for x in range(7):
        linked_list_1.add_to_beginning(x)

    # Print out some information about our linked list
    print("Length of linked_list_1: {}".format(len(linked_list_1)))
    print("linked_list_1 = {}".format(str(linked_list_1)))

    # Let's remove some elements from it and add some elements to the
    # beginning or end of it depending on whether those elements are
    # even or odd
    print("Removing elements from linked_list_1 and add some others to it...")
    linked_list_1.remove_value(3)
    linked_list_1.remove_value(5)
    for x in range(45, 61):
        if x % 2 == 0:
            linked_list_1.add_to_beginning(x)
        else:
            linked_list_1.append(x)

    # Let's print out the new values
    print("Length of linked_list_1: {}".format(len(linked_list_1)))
    print("linked_list_1 = {}".format(str(linked_list_1)))

if __name__ == '__main__':
    main()
