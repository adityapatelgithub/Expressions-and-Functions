class LinkedList:
    # The singly linked list Node
    class Node:
        __slots__ = "_value","_next"
        def __init__(self, v, n):
            self._value = v
            self._next = n
    #initialize the list
    def __init__(self):
        self._tail = None
        self._head = None
        self._length = 0
    #suport iteration though the list
    def __iter__(self):
        current = self._head
        while (current is not None):
            yield current._value
            current = current._next
    #Return the length of the list
    def __len__(self):
        return self._length
    #Print the values in the list by joing the values of the interation together
    def __str__(self):
        return "".join( list(iter(self)))
    #push a value onto the list
    def push(self,value):
        #Create a new node
        newNode = self.Node(value, None)
        #check if the list is empty. Otherwise, add it to the head
        if(self._head is None):
            self._head = self._tail = newNode
        else:
            newNode._next = self._head
            self._head = newNode
        self._length+=1
    #pop the head, and return the value
    def pop(self):
        val = self._head._value
        self._head = self._head._next
        self._length-=1
        return val
    #return the top value of the linked lsit without removing it
    def top(self):
        return self._tail._value
    #check if the list is empty
    def is_empty(self):
        return (self._length == 0)
    

