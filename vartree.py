# This class will represents a Map through a binarySearchTree
class binarySearchTree:
    class Node:
        __slots__ = "_var","_value", "_left", "_right"
        def __init__(self, left, var, value, right):
            self._var = var
            self._value = value
            self._left = left
            self._right = right
    def __init__(self):
        self._root = None
        self._length = 0
    #Make a tuple out of the nodes and tree
    def _rec_tuples(self, here):
        """Recursively convert tree into a tuple form"""
        if here is None:
            return ''
        else:
            return (self._rec_tuples(here._left),
                    here._var, self._rec_tuples(here._right))
    #Print out the tree
    def __str__(self):
        """Return a cleaned-up tuple version of the entire tree"""
        tuples = self._rec_tuples(self._root)
        return str(tuples).replace("''","None").replace(", ''","None")
    
    #def __str__(self):
    def __len__(self):
        return self._length
    
    #recursively search tree rooted 'here' for variable var
    def _search(self,here, var):
        if here is None:
            return None
        elif (here._var == var):
            return here
        elif (here._var > var):
            return self._search(here._left,var)
        elif (here._var < var):
            return self._search(here._right,var)
    
    # Check if the tree is empty.
    def is_empty(self):
        return (self._root is None)

    # Find and return the maximumvalue of the branch or tree
    def max(self, current):
        if (current._right is None):
            return current._value
        return self.max(current._right)
    
    #Do it recursively
    def _insert(self, here, var, value):
        if (here is None):
            newNode = self.Node(None, var, value, None)
            self._length +=1
            return newNode
        elif (here._var > var):
            return self.Node(self._insert(here._left,var,value),here._var,here._value, here._right)
        elif (here._var == var):    
            return self.Node(here._left, var, value, here._right)
        elif (here._var < var):
            return self.Node(here._left, here._var, here._value, self._insert(here._right,var,value))

        
    #Public method: assigning a value to a variable
    def assign(self, var, value):
        self._root = self._insert(self._root, var, value)

    #look up and retrieve value of a variable
    def lookup(self, var):
        temp = self._search(self._root,var)
        if(temp is None):
            self.assign(var,0)
            return 0
        else:
            return temp._value
            

