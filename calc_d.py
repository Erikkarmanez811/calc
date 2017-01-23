def lex(AS):
    """
    Функция которая лексер 
    """
    token = []
    tokens = []
    token1 = ''
    aS = list(AS)
    for i in aS:
        if i in operationss:
            
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
    elif oper == '(':
        a = 1
    elif oper == ')':
        a = 1
    else:
        print('error')
    print(oper,'это мой приоритет =',a)
    return(a)
    
        


while True:
    
    string = str(input())
    stack = []
    opz = []
    operationss = ['+' , '-'  , '*', '/','(', ')' ]
    operations = ['+' , '-'  , '*', '/']
    string = lex(string)
    print(string)
    string.append('^')
    op1 = ''
    op2 = ''
    opp1 = 0
    opp2 = 0
    for token in string:
        
        if type(token) == int:
            print(token,'я число')
            opz.append(token)
            print('изменилось опз   ', opz)


            
        if token in operations:
            print(token,'а я операция')
            
            if stack == []:
                print(token,'я первая операция')
                stack.append(token)
                print('изменилcя стэк   ', opz)
            else:
                print(token,'я не первая операция')
                op1 = token
                op2 = stack[-1]
                if prior(op1) > prior(op2):
                    print(token,'я операция чей приоритет выше, чем приоритет последней операции ')
                    stack.append(token)
                    print('изменилcя стэк   ', stack)

                       
                if prior(op1) <= prior(op2):
                    print(token,'я операция чей приоритет меньше или равен, чем приоритет последней операции ')
                    while prior(op2) >= prior(op1):
                        print('пока предидущие верно из стека в опз')
                        print('   ', stack)
                        op2 = stack.pop()
                        print('   ', stack)
                        opz.append(op2)
                        print('   ', opz)
                        if stack == []:
                            print('стек опустел из-за предидущего')
                            ssu = stack.pop()
                            stack.append(token)
                            print('   ', stack)
                            break
                        
                        if prior(op1) > prior(op2):
                            print('изначальное условие поменялось')
                            ssu = stack.pop()
                            stack.append(token)
                            print('   ', stack)
                            break
        
        if token == '(':
            print(token, 'я открывающая скобка')
            stack.append(token)
            print('   ', stack)
        if token == ')':
            print(token,'я закрывающая скобка')
            sap = stack.pop()
            print('    ',sap,'\n    ',stack)
            while prior(sap) != 1:
                opz.append(sap)
                print('    ', opz)
                sap = stack.pop()
                print(stack)
                            
                    
                        
                        
                    
        if token == '^':
            stack.reverse()
            for qwe in stack:
                opz.append(qwe)
            opz.append(ssu)
            while '(' in opz:
                opz.remove('(')
            print (opz)
            
        
    
    
        
    


























                
                
                
















                
                

        
                             
            
        








































        
