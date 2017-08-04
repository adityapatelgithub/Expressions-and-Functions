

def new_split_iter( expr ):
    """divide a character string into individual tokens, which need not be separated by spaces (but can be!)
    also, the results are returned in a manner similar to iterator instead of a new data structure
    """
    operators = ['+', '-', '*', '/', '%', '(', ')', '=', '<','>','!','?',':',';', ',']
    expr = expr + ";"                # append new symbol to mark end of data, for simplicity
    pos = 0                     # begin at first character position in the list
    while (expr[pos] != ";"):
        # Check for space. Skip if encounter
        if (expr[pos] == ' '):
            pos+=1
        #Check for variables
        elif(expr[pos].isalpha()):
            temp = pos
            while(expr[pos] not in operators and expr[pos] != ' '):
                pos+=1
            yield expr[temp:pos]
        # Check for numbers. Loop through until that number end then yield the number
        elif (expr[pos].isdigit()):
            temp = pos
            while(expr[pos].isdigit()):
                pos+=1
            yield expr[temp:(pos)]
        #Check some more 2 characther operator
        elif ((expr[pos] == '=' or expr[pos] == '!' or expr[pos] == '<' or expr[pos] == '>') and expr[pos+1]=='='):
            yield expr[pos]+expr[pos+1]
            pos+=2
        #Yield the rest (operators)!
        else:
            yield expr[pos]
            pos+=1
    yield ";"                             # inform client of end of data
