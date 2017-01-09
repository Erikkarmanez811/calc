def lex(AS):
    """
    Lexer function 
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
    opers = '()+-*/'
    if oper in opers:
        return opers.index(oper)
    print('Error')
    return 'Sad'
    

def rpn(exp):
    rpn = []
    stack = []
    
    for token in exp:
        if type(token) == int:
            rpn.append(token)
        


    if token in brackets:
            if token == '(':
                stack.append(token)
            if token == ')':
                sap = stack.pop()
                while sap != '(':
                    rpn.append(sap)
                    sap = stack.pop()
            
    if token in operations:
            if stack == []:
                stack.append(token)
            else:
                op1 = token
                op2 = stack.pop()


                while prior(op2) >= prior(op1):
                    rpn.append(op2)
                    op2 = stack.pop()


                    
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

                stack.append(token)

                            

                    
                        
                        
                    
        if token == '^':
            stack.reverse()
            for qwe in stack:
                opz.append(qwe)
            while '(' in opz:
                opz.remove('(')
            print (opz)    


        
operations = ['+' , '-'  , '*' , '/' ]
brackets = ['(',')']

print(prior('*'))
while True:
    exp = str(input())
    
    exp_l = lex(exp)
    print(exp_l)
    exp_l.append('^')
    op1 = ''
    op2 = ''
    opp1 = 0
    opp2 = 0
   
            
        
    
    
        
    


























                
                
                
















                
                

        
                             
            
        








































        
