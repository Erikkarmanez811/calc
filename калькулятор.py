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



def prior(oper):
    if oper == '+':
        a = 2
    elif oper == '-':
        a = 3
    elif (oper == '*') or (oper == '/'):
        a = 4
    elif (oper == '(') or (oper == ')'):
        a = 1
    else:
        print('error')
    return(a)
    
        


while True:
    string = str(input())
    stack = []
    opz = []
    operations = ['+' , '-'  , '(' , ')' , '*']
    string = lex(string)
    print(string)
    string.append('^')
    op1 = ''
    op2 = ''
    opp1 = 0
    opp2 = 0
    for token in string:
        if type(token) == int:
            opz.append(token)
        if token in operations:


            

            if stack == []:
                stack.append(token)
            else:
                op1 = token
                op2 = stack[-1]
                if prior(op1) > prior(op2):
                    stack.append(token)

                       
                if prior(op1) <= prior(op2):
                    while prior(op2) >= prior(op1):
                        op2 = stack.pop()
                        opz.append(op2)
                        if stack == []:
                           stack.append(token)
                           break
                        else:
                            if prior(op1) > prior(op2):
                                stack.append(token)
                                break

                            
        if (token == '(') or (token == ')'):
            if token == '(':
                stack.append(token)
            if token == ')':
                sap = stack.pop()
                while prior(sap) != 1:
                    opz.append(sap)
                    sap = stack.pop
                    
                        
                        
                    
        if token == '^':
            stack.reverse()
            for qwe in stack:
                opz.append(qwe)
            while '(' in opz:
                opz.remove('(')
            print (opz)
            
        
    
    
        
    


























                
                
                
















                
                

        
                             
            
        








































        
