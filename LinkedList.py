#!/usr/bin/env python
from __future__ import print_function

"""
In this exercise, follow along with text below sequentially instead of
going straight to the `main` method. The real work is going to take
place outside `main`.

Now that you've used things like lists and dictionaries in Python, i.e.,
"collections" or "containers" of "objects", I want to get more
fundamental for a second. Let's think about what, for example, a list
really is.

Thought Experiment (spend a few minutes before moving on): If you wanted
to create a list in Python, you would just write something like,
"l = []", and then start to append items or extend the list, etc. But,
what if you were asked to make a list and not use the brackets (i.e.,
don't use Python's built-in list type or any other container for objects
that Python provides, such as dictionaries, etc.)? Think about how you
might try to represent the idea of a list if you couldn't actually make
a Python list. A really naive way of doing it would be to make variables
to store each value, i.e.,

>>> first = 5
>>> second = 4
>>> third = 9

But you see the issue here. There's no actual collection of objects and
there's no ordering or relation between the objects. So, how might you
represent this information?

- Linked Lists
A key building block in computer science is the concept of a linked
list, i.e., a collection of objects whose elements are linked together
so as to form a representation of a list. For example, consider the
situation above where we had defined the `first`, `second`, and `third`
variables. Imagine that each of these variables actually stored not only
a value, but also a "link", i.e., `first` would store its value and a
link to `second`, `second` would store its value and a link to `third`,
and `third` would store its value and a link whose value was None (since
it's the last element). This is the basic idea behind a linked list.
This assignment will be about making a linked list implementation and
using it rather than Python's own list implementation (which is much
better and faster but is built utimately using the same kind of
implementation at some deep level).

What we need first is to create a custom type of "object" that will
represent a "node" in the list. Let's call it `Node`. This object will
have a couple attributes that can be changed: a `value` attribute (which
will store the value of list element, i.e., 5.8 or 19 or "the") and a
`next_node` attribute, which will store a reference to the next node (if
one exists). Below I will define a class for use in this assignment just
to start it off.
"""

class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

"""
The `__init__` method is a required method (not technically, but for our
purposes, let's just say it is) that you have to define for a Python
class. It gets called when an object of type `Node` is instantiated. A
`value` for the node and a reference to the following node can be passed
in, but both are technically optional (when you want to give a default
value to a parameter, you can specify the default value via
`value=None`, for example, in the function signature). What would happen
if I just created an object of type `Node` via "a = Node()"? What would
`a`'s `value` attribute be equal to (i.e., `a.value`)? And what would
`a.next_node` be equal to? Both would be equal to None since I did not
specify a value for either parameter. With this implementation of
`Node`, I could execute the following:

>>> third = Node(value=7.2, next_node=None)
>>> second = Node(value=6.7, next_node=third)
>>> first = Node(value=1.0, next_node=second)

This gives us a basic "linked list". As long as I have a reference to
the first element, I can traverse the list to get to the other elements.
For example:

>>> i = 0
>>> current_node = first
>>> # Keep on iterating until breaking
>>> while True:
...     # Print `node`'s value and index
...     print("Node {}: {}".format(i, current_node.value))
...     # Check if current node is the last node
...     if current_node.next_node is None:
...         break
...     # Update `current_node`
...     current_node = current_node.next_node
...     # Increment i
...     i += 1

This would print out the following:

    Node 0: 1.0
    Node 1: 6.7
    Node 2: 7.2

Now that we have a class to represent each node in the linked list,
there are just a couple other points to mention before implementing the
actual linked list class. Firstly, it is customary to implement a sort
of "header" node, which can be understood as a node that does not have a
value and whose only function is to point to the "real" first node. When
passing around a reference to a linked list, it will be necessary to
figure out where to start. Next, the implementation of `LinkedList` will
have to contain many of the methods for doing things like adding
elements to the list, deleting them, etc., that make it useful as a data
structure. The main part of this assignment will be to extend the
`LinkedList` class below to add functionality to it and then to use this
functionality in a real program. I will start off the implementation by
making the `__init__` method and some other methods and then I will add
so-called "stub" methods (unimplemented methods) that you will have to
fill out yourself. Read all of the code and documentation for
`LinkedList`, familiarize yourself with how it works, and fill in the
sections that call for it.

To view a diagram of a linked list, check out the following URL:

    http://people.engr.ncsu.edu/efg/210/s99/Notes/LLdefs.gif

This diagram shows a linked list represented as a header node pointing
to the first node, which is an object that contains a value and a link
to the next node, and then the next node and then the final node, which
contains a value, but has a link that is null (i.e., signifying that
there is no next node).

Implementing the linked list data structure, however, is not just about
implementing the structure itself as it is about implementing the ways
that the data structure can be interacted with. In other words, what use
is a linked list implementation if you can't add new data to it? Or if
you can't remove data from it? Or find data in it? As you will see
below, the bulk of this exercise is implementing the interface between
the user and the data structure. This will require a thorough
understanding of the linked list structure, so please study the diagram
linked to above and study the `Node` class and the idea of a "header"
node. All of this will be important as we implement the functionality of
the linked list class.

Before we get to that part, I want to take a second to just outline what
we need to do (and it's a little open-ended, so bear with me). What do
you think the main things are that you would need to be able to do in
order for the linked list implementation to be worthwhile? Well, the
obvious things that we need to be able to do are inserting and removing
elements. With Python's `list` type, elements can be `append`ed onto the
end, `extend`ed from the end, `insert`ed at particular indices,
`pop`ped off the end, and `del`eted. So, we should implement an `append`
method that will append an element to the end of the list, perhaps. This
will allow us to construct a linked list starting with an empty list,
i.e., just ceate one and then start appending elements to it just like
with a Python `list`. Let's also implement a `pop` method that removes
an element from the end of the list and returns its value. In fact,
maybe we should have two `pop` methods, one for popping elements off the
end and the other for popping elements off the beginning. Furthermore,
it would be nice to remove an element from index or to remove a
particular value wherever it occurs. So, this will all be decided during
our implementation of the linked list class.

- Notes
  1. In Python classes, most methods/functions will take a first
     argument called `self`. Notice how, when I wanted to make a `Node`
     object, for example, I did not need to specify `self` even though
     it shows up in the method signature,
     "def __init__(self, value=None, next_node=None)". I could make a
     new node just by executing "Node(value=3.4)" or even just "Node()".
     The `self` argument refers to the instantiation of the class
     itself. That's why in the method you see things like
     "self.value = value". This is setting the object's `value`
     attribute to the value of the passed-in parameter (also named)
     `value`. Don't think too much about what `self` is. Just use it as
     you see it used here. But do NOT forget it. Things will break if
     it's not included.
  2. The text included inside the three double quotation marks here as
     elsewhere (i.e., inside the actual code) is documentation. It
     doesn't have to be there at all, but it's just good practice to
     include it to describe how things work. When it's included in
     functions/methods, it's often used to spell out the meaning of
     parameters, what type they are expected to have, etc., as well as
     return values/types (if any).
"""

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
        Return False if the list contains any elements; True otherwise.

        :returns: boolean value
        :rtype: bool
        """

        # Check if the object's `header_node` attribute actually points
        # to a node (i.e., its `next_node` attribute is not equal to
        # None)
        if self.header_node.next_node is None:
            return True
        return False

    def push(self, new_value):
        """
        Add new node with the given value to the start of the list,
        "pushing" or shifting all other nodes one index forward.

        :param new_value: new value to add to the beginning of the list
        :type new_value: object
        """

        # Create a new Node and set its `value` attribute to the given
        # value and set its `next_node` attribute to the value of the
        # current first node in the list, all of which can be done by
        # passing in parameter values when instantiating the new node)
        new_node = Node(value=new_value, next_node=self.header_node.next_node)

        # Now, set the value of `header_node`'s `next_node` attribute to
        # point to this new node
        self.header_node.next_node = new_node


    def append(self, new_value):
        """
        Append new value to the end of the linked list.

        This is doing something very similar to what `push` is doing:
        it adds a new value to the list, but it tacks it onto the end
        rather than onto the beginning. The advantage of `push` is that
        there is no need to traverse the list to find the last node: it
        simply reassigns the header node's `next_node` attribute to
        point to it instead of the current first node and its own
        `next_node` link points to the that formerly-first node, thereby
        shifting that node one index forward (and all nodes that follow
        it). If the list is empty, then this new node's link will
        actually be None since it will be the one and only node (other
        than the header node, of course) in the list.
        
        :param new_value: new value to append to list (inside a node)
        :type new_value: object (basically, this means any type)
        """

        # Start at the beginning of the linked list, which can be
        # reached via the object's `header_node` attribute
        current_node = self.header_node
        while True:

            # Check if this node happens to be the last node in the
            # list, in which case we have found the location we need to
            # modify
            # Note: This would even work for an empty linked list since
            # the value of `header_node`'s `next_node` attribute is None
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

            # Otherwise, move to the next node
            else:
                current_node = ### FILL IN

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
        # object's `header_node`'s `value` attribute is equal to None
        if ### FILL IN:
            return ### FILL IN (i.e., what value should be returned?)

        # If the list is not empty, let's start at the first real node,
        # i.e., the node that is pointed to by `header_node.next_node`
        current_node = ### FILL IN

        # Loop through the elements of the list and keep a counter for
        # the index
        index = 0
        while True:
            
            # If the value of the current node is equal to the value
            # we're trying to find, then return the value of `index`
            # since we're finished
            if current_node.value == ### FILL IN:
                return ### FILL IN (i.e., what value should be returned?)

            # Otherwise, check if this is the last node and, if so,
            # return -1 since that means the value was nowhere to be
            # found
            if current_node.next_node is None:
                return ### FILL IN (i.e., what value should be returned?)

            # Move forward one node and increment the counter
            # Note: Notice that I am not using an `else` statement here
            # (or even above after the second `if` block). Why/how can I
            # do this? The reason is that the `if` condition, if met,
            # would lead to a situation where the code below it would
            # never be executed. Thus, logically, there is no need to
            # put an `else` statement. This is naturally an `else`
            # statement.
            current_node = ### FILL IN
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
    # >>> x = LinkedList()
    # >>> x.push(5)
    # >>> x.push(6)
    # >>> print(len(x))
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
        # a counter and set it to 0 and iterate over the list's elements
        # until you get to the element whose `next_node` value is equal
        # to None (i.e., the last element).

    def __str__(self):
        """
        Return a string representation of the linked list object.

        :returns: string representation of the linked list object
        :rtype: str
        """

        str_repr = ""

        # Add string representations of the linked list's values
        # themselves to the string representation of the linked list
        if not self.is_empty():
            current_node = self.header_node.next_node
            while True:

                # Concatenate the string value of the current node's
                # value to the string representation of the linked list
                # object
                if str_repr != "":
                    str_repr = ", ".join([str_repr, str(current_node.value)])
                else:
                    str_repr = str(current_node.value)
                
                # Break if the current node is the last node
                if current_node.next_node is None:
                    break
                
                # Move forward to next node
                current_node = current_node.next_node

        # Wrap the elements string in double braces
        str_repr = "[[{}]]".format(str_repr)

        return str_repr

    def remove_value(self, value_to_remove):
        """
        Find and remove the first occurrence of the given value and
        return True if the removal was successful or False if the value
        could not be located anywhere in the list.

        :param value_to_remove: value to find/remove in the list
        :tyep value_to_remove: object

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
        # do is set the value of `prev_node.next_node` to the value of
        # `prev_node.next_node.next_node`, i.e., skipping over a whole
        # node. You don't need to do anything else. Removing the
        # reference to a node is the same as deleting it (i.e., Python
        # will take care of actually deleting it and freeing up the
        # memory).
        # I will start it off for you:
        
        # If it's empty, return False since there's nothing to remove
        if self.is_empty():
            return False

        # Get the index of the value to remove
        ### HINT: Use the `find_index_of_value` function to 1) see if
        ###       the value is even in the list (remember, that function
        ###       will return -1 if it can't find the value in the list)
        ###       and 2) get the index of the value in the list.
        value_to_remove_index = ### FILL IN

        # If `value_to_remove_index` is -1, that means the value was not
        # found, so return False
        ### FILL IN

        # Now traverse the list until you get to the node that is
        # directly preceding the node you want to remove. (Remember to
        # break out of this loop or it will run forever!)
        current_node = ### FILL IN
        current_index = ### FILL IN
        while True:

            # If we're at the node before the node we want to remove,
            # we can stop and do the removal
            if ### FILL IN:

                current_node.next_node = ### FILL IN
                return ### FILL IN (i.e., what value should be returned?)

            current_node = ### FILL IN
            current_index += 1

    def subsequence(self, i, j):
        """
        Return a new `LinkedList` object that consists of the elements
        in the object's linked list that are from index `i` up to (but
        not including) index `j`. If `j` represents a value that is
        larger than the length of the linked list, just include the rest
        of the list.

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
        if not all(isinstance(x, int) for x in [i, j]):
            raise ValueError("Parameters i and j should be integer values.")

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
            return ### FILL IN (i.e., what value should be returned?
                   ### Hint: you need to return a new linked list, so
                   ### make one.)

        # Ok, now you will do the rest. Basically, you're going to need
        # to make a new `LinkedList` here and append each element
        # starting at index `i` in the current linked list and ending
        # right before index `j` (or ending when the linked list ends,
        # whichever comes first).

        subsequence_list = ### FILL IN (Hint: Make a new linked list object.)
        current_node = ### FILL IN
        current_index = 0
        while current_index < j:
            
            ### IMPLEMENT THE REST OF THIS LOOP

        return subsequence_list

    def pop_from_beginning(self):
        """
        Remove and return the value of the first node (after the header
        node).

        :returns: value of first node
        :rtype: object
        
        :raises ValueError: if list is empty
        """

        ### IMPLEMENT THIS
        # Hint: If there is at least one element to pop off the list,
        # get the value of `header_node.next_node.value` and store it in
        # a variable and then set `header_node.next_node` to
        # `header_node.next_node.next_node`. Then, return the value that
        # you stored in a variable. If the list is empty, raise an
        # error. I will do this check for you.

        # Check if the list is empty, in which case there's no node to
        # remove/return
        if self.is_empty():
            raise ValueError("Linked list is empty!")

        # Implement the rest of this function.

    def pop_from_end(self):
        """
        Remove and return the value of the last node.

        :returns: value of first node
        :rtype: object

        :raises ValueError: if list is empty
        """

        ### IMPLEMENT THIS
        # Hint: Traverse the list until you're at the node before the
        # last node. Then, get the value of the last node and set the
        # second-to-last node's `next_node` attribute to None (since
        # now it is the last node). Again, if the list is empty, there
        # is nothing to remove/return. Raise an exception like I did
        # above if the list is empty.

    def delete_index(self, index):
        """
        Remove the element at the given index, shifting all succeeding
        elements back by one. Return True if successful; False
        otherwise.

        :param index: index (starting from zero) of element to remove
        :type index: int

        :returns: boolean value confirming that the deletion was
                  successful (or unsucessful)
        :rtype: bool
        """

        ### IMPLEMENT THIS
        # Hint: Traverse the list like usual, but keep a counter. Stop
        # at the index before the one we want to remove. Make that
        # element's `next_node` attribute point to the node following
        # the element we want to delete (or to the value None if the
        # element we want to delete happens to be the last element in
        # the list). Return True. If the index is never reached (i.e.,
        # because the linked list is too small), return False.
        # I'll start you off like usual.

        # Return False if the linked list is empty
        if self.is_empty(): return False

        # Traverse list and stop when counter is one less than `index`
        i = 0
        current_node = self.header_node
        while True:

            # Stop if `i` is one less than `index
            if i == index - 1:
                ### FIGURE OUT WHAT TO DO HERE
                ### Remember to return True when finished

            # Stop if `current_node.next_node` is None (i.e., it's the
            # last node in the list) and return False since there's no
            # more nodes to traverse
            elif ### IMPLEMENT THIS
                ### IMPLEMENT THIS
            else:
                ### Increment `i`
                ### Change `current_node` to point to next node

    """
    Just for fun/extra credit, implement a "magic" Python method called
    `__add__`. When implemented, this will enable one to "add" two
    linked list instances together in a way similar to the way that one
    can add together two lists in Python, e.g.:

    >>> [1, 2, 3] + [4, 5, 6]      # [1, 2, 3, 4, 5, 6]

    Implementing the `__add__` method will not just enable this
    capability in a general sense, it will actually enable a user to use
    the `+` operator directly two add two linked lists together. Isn't
    that so awesome?
    """
    def __add__(self, linked_list_1, linked_list_2):
        """
        Link two linked lists together to make a larger linked list.

        :param linked_list_1: first linked list
        :type linked_list_1: LinkedList
        :param linked_list_2: second linked list
        :type linked_list_2: LinkedList

        :returns: combined linked list
        :rtype: LinkedList
        """

        ### IMPLEMENT THIS METHOD. YOU'LL GET NO HELP FROM ME.
        ### Alright, fine, a little help. Simply create a new linked
        ### list and then iterate over the first and then the second
        ### of the linked lists and simply append new values to the new
        ### linked list until you've traversed both lists. Then, return
        ### the new linked list. In fact, it should be easy to make this
        ### method accept any number of parameters, chaining the linked
        ### lists together and returning a new combined linked list.
        ### Consider how this might be done.


def main():

    # Let's make some linked lists using our implementation

    # 1. First we'll make a linked list and add some elements to it by
    #    using the `push` method. Recall that this means that each
    #    time we add an element to the list it will be "pushed" onto the
    #    beginning of the list, shifting any other elements back one
    #    index. This is the opposite of the `append` method, which does
    #    the same thing Python lists' `append` method does.
    linked_list_1 = LinkedList()

    # For each number in the range from 0 up to (but not including) 7,
    # push the number onto the beginning of our (currently) empty linked
    # list
    for x in range(7):
        linked_list_1.push(x)

    # Print out some information about our linked list
    # Remember that we can print out a string representation of our
    # linked list since we implemented the `__str__` method in the
    # `LinkedList` class.
    print("Length of linked_list_1: {}".format(len(linked_list_1)))
    print("linked_list_1 = {}".format(str(linked_list_1)))

    # Now let's remove some elements from it and add some elements to
    # the beginning or end of it depending on whether those elements are
    # even or odd
    print("Removing elements from linked_list_1 and adding some others to "
          "it...")
    linked_list_1.remove_value(3)
    linked_list_1.remove_value(5)
    for x in range(45, 61):
        if x % 2 == 0:
            linked_list_1.push(x)
        else:
            linked_list_1.append(x)

    # Let's print out the new values
    print("Length of linked_list_1: {}".format(len(linked_list_1)))
    print("linked_list_1 = {}".format(str(linked_list_1)))

    # 2. Now let's make a big linked list that includes words instead of
    #    numbers. We'll then search for some values in it, remove some
    #    values, get some subsequences, etc.
    linked_list_2 = LinkedList()

    with open('data/pride_and_prejudice.txt') as text_file:
        for line in text_file.readlines():
            
            # Preprocess the line by stripping off whitespace and
            # converting all letters to lower-case
            line = line.strip().lower()

            # Skip empty lines
            if line == "": continue

            # Now let's split the line on whitespace and add each word
            # to the linked list as a separate element
            for word in line.split():

                # FILL IN
                # Hint: I'll let you decide which way you want to add
                # each word to `linked_list_2`, but be aware that using
                # one will be much faster than using the other. Do you
                # know which one will be faster and why?

    print("Length of linked_list_2: {}".format(len(linked_list_2)))

    # Now that we have a pretty big linked list, let's search for some
    # values that are probably in it and some that are probably not in
    # it
    print("Searching linked_list_2 for the word 'big'...")
    ### Search for the word "big" in `linked_list_2` and, if found,
    ### print out the index at which it occurs (which will be returned
    ### by the function). If it is not found, the return value of the
    ### function will be -1. So, it will be necessary to first get the
    ### return value and then to see if it's not -1. If it is -1, then
    ### print out a message that the word was not found.

    ### Repeat this for the following words: "small", "hate", "table",
    ### "plant", "stove", "yard", "umbrella", "jacket", "coffee". For
    ### each word, first print out the message "Searching linked_list_2
    ### for the word 'x'..." where `x` refers to the word being searched
    ### for. It is probably best if you do this in a for loop rather
    ### than writing the same code 8 or 9 times. I'll start you off.
    words = ["small", "hate", "table", "plant", "stove", "yard", "umbrella",
             "jacket", "coffee"]
    for word in words:

        ### PRINT OUT THE MESSAGE INDICATING WHAT WORD IS BEING SEARCHED
        ### FOR. THEN, SEARCH FOR THE WORD AND PRINT OUT THE INDEX AT
        ### WHICH IT OCCURRED OR, IF IT DOESN'T OCCUR, PRINT OUT A
        #### MESSAGE SAYING SO.

    # Now let's try the same thing but with some words that surely will
    # not show up (at least probably)
    words = ["internet", "python", "camry"]
    for word in words:

        ### FILL IN. DO THE SAME THING AS YOU DID ABOVE.

    # Now let's remove some words just for fun. Let's remove all
    # occurrences of the word "him". Since the `remove_value` function
    # will remove the first occurrence of the passed-in value and return
    # True or False (indicating whether a removal actually took place),
    # we can just keep on trying to remove a word until the return value
    # is False. Once that's the case, all instances of that word have
    # been removed. Since "him" most definitely occurs in the text, we
    # can skip the check to see if it occurs. If you would like to do
    # this, you get some extra credit and a sticker.
    while True:

        removed_him = ### FILL IN THIS LINE SO THAT THE WORD `him` IS
                      ### PASSED IN TO `remove_value`.
        
        # If the return value is False, we know all occurrences of the
        # word are now gone since the word couldn't be removed
        # successfully (i.e., because it couldn't be found), so that
        # means we can break.
        if removed_him is False:
            break

    # Now that all occurrences of the word "him" have been removed
    # (cleaned?) from the `linked_list_2`, let's try to find the word
    # "him" in it.
    found_him = ### FILL IN

    # Now also let's print out the length of `linked_list_2`. It should
    # be quite different from the original value we printed out above
    # since less words are contained in the list.

    # Now let's try to get some subsequences within `linked_list_2`
    i = 67
    j = 89
    
    # Use the `subsequence` function of the linked list to get the
    # subsequence of `linked_list_2` from `i` up to `j`.
    part_of_linked_list_2 = ### FILL IN

    ### PRINT OUT THE SUBSEQUENCE AND ITS LENGTH

    print("Program complete!")


if __name__ == '__main__':
    main()
