from vartree import binarySearchTree
from peekable import Peekable, peek
from newsplit import new_split_iter
from infixtotree import to_expr_tree, define_func

def evaluate(expr):
    """Define a new function, or evaluate an expression

    If the first word in the line "deffn", it should appear as
          deffn <function name> ( <parameters> ) = <function body>
          a VarTree will associate the function name with
            a list of parameters (at least one, maybe more)
            and a tree representing the function body
    otherwise the input line is evaluated in an expression tree
    """
    iterator = Peekable(new_split_iter(expr))
    if peek(iterator) == "deffn":
        name, parms, body = define_func(iterator)
        functions.assign(name, (parms, body))
    else:
        print(expr,':',to_expr_tree(expr).evaluate(variables, functions))

functions = binarySearchTree()
variables = binarySearchTree()