
from peekable import Peekable, peek
from newsplit import new_split_iter
from exprtree import Oper, Cond, Var, Value, Func
#eval equal sign
relaOpers= ['<','>','>=','<=','==','!='];
operators = ['+', '-', '*', '/', '%', '(', ')', '=', '<','>', '>=', '<=', '==', '!=','!','?',':',';'];
def tree_assign(iterator):
    temp = tree_conditional(iterator)
    peeking = peek(iterator)
    if(peeking == '='):
        next(iterator)
        temp = Oper(temp,peeking,tree_assign(iterator))
        peeking = peek(iterator)
    return temp
def tree_conditional(iterator):
    temp = tree_relational(iterator)
    peeking = peek(iterator)
    if(peeking == '?'):
        next(iterator)
        case1 = tree_relational(iterator)
        next(iterator)
        case2 = tree_relational(iterator)
        temp =Cond(temp,case1,case2)
    return temp
def tree_relational(iterator):
    temp = tree_sum(iterator)
    peeking = peek(iterator)
    if(peeking in relaOpers):
        next(iterator)
        temp = Oper(temp,peeking,tree_sum(iterator))
        peeking = peek(iterator)
    return temp
#eval sum
def tree_sum(iterator):
    # evaluate the first term while checking for the next term for multiplication
    temp = tree_product(iterator)
    #store the operator
    #this while loop evaluates sum and subtraction.
    #yield data back up from product then yield the sign like postfix
    peeking = peek(iterator)
    while (peeking == '+' or peeking == '-'):
        next(iterator)
        temp = Oper(temp,peeking,tree_product(iterator))
        peeking = peek(iterator)
    # skip the ')' and continue changing the expression
    #if(peeking == ')'):
    #    next(iterator)
    return temp  
#yield multiplication        
def tree_product(iterator):
    #call factor to evaluate order of operation
    temp= tree_factor(iterator)
    peeking = peek(iterator)
    #this while loop evaluates product and multiplication
    #yield data back up from factor then yield the sign like postfix    
    while(peeking == '*' or peeking == '/' or peeking == '%' or peeking == '//'):
        next(iterator)
        temp = Oper(temp,peeking,tree_factor(iterator))
        peeking = peek(iterator) 
    return temp
#yield factor     
def tree_factor(iterator):
    peeking = peek(iterator)
    #check negative
    if(peeking == '-'):
        next(iterator)
        temp = tree_factor(iterator)
        return Value(int('-'+temp.__str__()))
    #check open parathesis
    if(peeking == '('):
        next(iterator)
        temp =tree_assign(iterator)
        next(iterator)
        return temp
    else:
        temp = next(iterator)
        if(temp[0].isalpha() and peek(iterator) == '('):
            parms = [];
            next(iterator)
            while(peek(iterator) not in operators):              
                if(peek(iterator) != ','):                   
                    parms.append(tree_assign(iterator))
                else:
                    next(iterator)
            next(iterator)
            return Func(temp, parms)
        elif(temp[0].isalpha()):
            return Var(temp)
        else:
            return Value(temp)

def to_expr_tree( expr ):
    return tree_assign(Peekable(new_split_iter(expr)))

def define_func( expr ):
    #getting the name of the function
    next(expr)
    name = next(expr)
    next(expr)
    
    #getting the parameters for the function
    parms = [];
    while(peek(expr)!= ')'):
        if(peek(expr)!= ','):
            parms+= next(expr)
        else:
            next(expr)
    #getting the body of the function
    next(expr)
    next(expr)
    body = tree_assign(expr)

    return name, parms, body

