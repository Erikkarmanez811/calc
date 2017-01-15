def lex(AS):
    """
    Lexer function 
    """
    token = []
    tokens = []
    token1 = ''
    aS = list(AS)
    for i in aS:
        if i in operations + brackets:
            
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

                
                op2 = stack.pop()

                while prior(op2) >= prior(token):
                    rpn.append(op2)
                    if len(stack):
                        op2 = stack.pop()
                    else:
                        break


                    
                if prior(op2) < prior(token):
                    stack.append(op2)

                stack.append(token)
  
    while len(stack):
        rpn.append(stack.pop())
    return rpn
            

def evaluate(rpn_exp):
    stack = []
    for elem in rpn_exp:
        if type(elem) == int:
            stack.append(elem)
        if elem == '+':
            stack.append(stack.pop()+stack.pop())
        if elem == '-':
            stack.append(-stack.pop()+stack.pop())
        if elem == '*':
            stack.append(stack.pop()*stack.pop())
        if elem == '/':
            stack.append(1/(stack.pop()/stack.pop()))
    return stack.pop()


        
operations = ['+' , '-' , '*' , '/' ]
brackets = ['(',')']

while True:
    exp = str(input())
    
    exp_l = lex(exp)
    
    rpn_exp = rpn(exp_l)

    print(evaluate(rpn_exp), 'result')
