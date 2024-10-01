#!/usr/bin/python3
"""Class For Linked List"""


class Node:
    """Sinlge Linked List Class"""

    def __init__(self, data, next_node=None):
        """Function to Initialize Object"""
        if type(data) is not int:
            raise TypeError("data must be an integer")
        if next_node is not None or type(next_node) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__data = data
        self.__next_node = next_node

        @property
        def data(self):
            """Function to get data"""
            return (self.__data)

        @data.setter
        def data(self, value):
           """Function to set new data"""
           if type(value) is not int:
              raise TypeError("data must be an integer")
           self.__data = value

        @property
        def next_node(self):
            """Function to retrieve next node"""
            return (self.__next_node)

        @next_node.setter
        def next_node(self, value):
            if value is not None or isinstance(value, Node) is not True:
                raise TypeError("next_node must be a Node object")
            self.__next_node = value


"""Linked List Class"""


class SinglyLinkedList:
    """Sinlge Linked List Class"""
    def __init__(self):
        """Initialize head of list"""
        self.__head = None

    def sorted_insert(self, value):
        """Insert New Node (sorted)"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        current = self.__head
        prev = current
        while current is not None:
            if current.data > value:
                break
            prev = current
            current = current.next_node
        new_node = Node(value, current)
        if current == self.__head:
            self.__head = new_node
        else:
            prev.next_node = new_node
            prev.next_node = new_node
