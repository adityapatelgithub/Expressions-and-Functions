

from linkedlist import LinkedList
from vartree import binarySearchTree
from infixtotree import to_expr_tree

#create a varTree to store variables
varTree = binarySearchTree()
# evaluate postfix expression

def eval_postfix(postfixExpr):
    #print(list(postfixExpr))
    #create a stack to store operands
    stack = LinkedList()
    # iterate through the postfix iterator
    for i in postfixExpr:
        #check operand and append to stack.
        #if operator, evaluate the last 2 terms in the stack and push it back
        if(i[0].isdigit() or i[0].isalpha()):
            stack.push(i)
        #check for assignment operator
        elif(i == '='):
            top = stack.pop()
            bottom = stack.pop()
            if(top[0].isalpha()):
                top = varTree.lookup(top)
            #print("bottom: ", bottom, " Top: ", top)
            varTree.assign(bottom,top)
            stack.push(bottom)
        #hit operator => evaluate expression
        else:
            top = stack.pop()
            bottom = stack.pop()
            #if it is a variable, then search from the binary tree
            if(top[0].isalpha()):
                top = varTree.lookup(top)
            if(bottom[0].isalpha()):
                bottom = varTree.lookup(bottom)
            temp = eval(str(bottom) + i + str(top))
            stack.push(str(temp))
    if(stack.top()[0].isdigit()):
        return float(stack.top())
    return varTree.lookup(stack.top())


