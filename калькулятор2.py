def lex(AS):
    """
    Функция которая лексер 
    """
    token = []
    tokens = []
    token1 = ''
    aS = list(AS)
    for i in aS:
        if i in operations:
            
            if token != []:
                for q in token:
                    token1 += q
                token1 = int(token1)
                tokens.append(token1)
                token = []
                token1 = ''
                
            tokens.append(i)
        else:
            token.append(i)
    else:
        if token != []:
            for q1 in token:
                token1 += q1
            token1 = int(token1)
            tokens.append(token1)
            token = []
            token1 = ''       
    return (tokens)



def prior(op):
    if (op == '+') or (op == '-'):
        return(2)
    if op == '*':
        return(3)
    if (op == '(') or (op ==')'):
        return(1)
        



string = str(input())
stack = ['^']
opz = []
operations = ['+' , '-'  , '(' , ')' , '*',]
string = lex(string)
string.append('^')
print(string)
op1 = ''
op2 = ''
opp1 = 0
opp2 = 0
for token in string:
    if (stack[-1] == '^') and ((type(token) == int) or (token == '+' or '-' or '*')):
        stack.append(token)
        continue
    if token == '(':
        stack.append(token)
        continue
    if (stack[-1] == '^') and (token == '^'):
        print('все')
        continue 
    if (stack[-1] == '^') and (token == ')'):
        print('ошибка')
        break


    if (stack[-1] == '+') and ((token == '^' or '+' or ')') or (type(token) == int)):      
        sp = stack.pop()
        opz.append(sp)
        continue
    if (stack[-1] == '+') and (token == '*'):
        stack.append(token)
        continue


    if (type(stack[-1]) == int) and ((token == '^' or '+' or ')') or (type(token) == int)):
        sp = stack.pop()
        opz.append(sp)
        continue
    if (type(stack[-1]) == int) and (token == '*'):
        stack.append(token)
        continue


    if (stack[-1] == '*') and ((token == '^' or '+' or ')' or '*') or (type(token) == int)):
        sp = stack.pop()
        opz.append(sp)
        continue
        

    if (stack[-1] == '(') and ((token == '+' or '*') or (type(token) == int)):
        stack.append(token)
        continue
    if (stack[-1] == '(') and (token == ')'):
        deL = stack.pop()
        continue
    if (stack[-1] == '(') and (token == '^'):
        print('ошибка')
        break
else:
    for qwe in stack:
        opz += qwe
    print(opz)
        
    
        
        
        
        
        
    
        
        
        
    
    
        
    


























                
                
                
















                
                

        
                             
            
        








































        
