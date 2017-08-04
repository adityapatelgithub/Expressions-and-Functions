from abc import ABCMeta, abstractmethod
from vartree import binarySearchTree

#This tree will store the operands and operators and return inorder or postorder tracing
class ExprTree(metaclass = ABCMeta):
    def __str__(self):
        return ' '.join( str(x) for x in iter(self))

    #@abstratmethod
    def __iter__(self):
        """an inorder iterator for this tree node, for display"""
        pass

    #@abstractmethod
    def postfix(self):
        #Posst order iteration to create a postfix expression
        pass
        
    #@abstractmethod
    def evaluate(self, variables, functions):
        """evaluate using the existing variables"""
        pass

class Value(ExprTree):
    def __init__(self, v):
        self._value = v
    def __str__(self):
        return self._value
    def __iter__(self):
        yield self._value
    def postfix(self):
        yield self._value
    def evaluate (self, variables, functions):
        return self._value
class Var(ExprTree):
    """ A variable leaf"""
    def __init__(self,n):
        self._name = n
    def __str__(self):
        return self._name
    def __iter__(self):
        yield self._name
    def postfix(self):
        yield self._name
    def evaluate(self, variables, functions):
        
        return variables.lookup(self._name)


#Take in two operands and an operator
class Oper(ExprTree):
    __slots__ = "_op1","_operator","_op2"
    def __init__(self, op1, operator, op2):
        self._op1 = op1
        self._operator = operator
        self._op2 = op2
    def __str__(self):
        return super().__str__()
    def __iter__(self):
        yield '('
        yield from self._op1
        yield self._operator
        yield from self._op2
        yield ')'
    def postfix(self):
        yield from self._op1.postfix() 
        yield from self._op2.postfix()
        yield self._operator
    def evaluate(self, variables, functions):
        evalop1=self._op1.evaluate(variables,functions)
        evalop2=self._op2.evaluate(variables,functions)        
        if(self._operator == '='):
            variables.assign(self._op1.__str__(), evalop2)
            return evalop2
        else:
            return eval(str(evalop1) + str(self._operator) + str(evalop2))
#This class takes in a condition, and two answers based on that condition
class Cond(ExprTree):
    __slots__ = "_cond", "_op1","_op2"
    def __init__(self,cond, op1, op2):
        self._cond = cond
        self._op1 = op1
        self._op2 = op2
    def __str__(self):
        return super().__str__()
    def __iter__(self):
        yield from self._cond
        yield '?'
        yield from self._op1
        yield ':'
        yield from self._op2
        
    def postfix(self):
        pass
    def evaluate(self, variables, functions):
        if(self._cond.evaluate(variables, functions)):
            return self._op1.evaluate(variables, functions)
        else:
            return self._op2.evaluate(variables, functions)
        
#This class will support function call
class Func(ExprTree):
    __slots__ = "_name","_parms"
    def __init__ (self, name, parms):
        self._name = name
        self._parms = parms
    def __str__(self):
        return super().__str__()
    def __iter__(self):
        yield self._name
        yield '('
        yield from self._parms
        yield ')'
    def postfix(self):
        pass
    def evaluate(self, variables, functions):
        parms, body = functions.lookup(self._name)
        #print(self._parms[0], " " , parms[0])
        for i in range(0,len(parms)):
            variables.assign(parms[i], self._parms[i].evaluate(variables, functions))
        return body.evaluate(variables, functions)
        #functions vartree incldes (name, (parms, body))

