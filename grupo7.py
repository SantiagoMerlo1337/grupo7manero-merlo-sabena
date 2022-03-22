def calculator(input_operation):
    resultado = [0,0]
    resultado[0] = eval(input_operation)
    c1=0
    c2=0
    max=0
    for i in input_operation:
        if i == "(":
            c1+=1
        elif i == ')':
            c2+=1
        if max<c1-c2:
            max = c1-c2
    c1 = 0
    c2=0
    flag=0
    for x in input_operation:
        if flag==0:
            if x == '(':
                c1+=1
            elif x == ')':
                c2+=1
            if max == c1-c2:
                operacion=''
                flag=1
        else:
            if x == ')':
                break
            operacion += x
    resultado[1]= operacion

    return resultado
entrada = input()
entrada = calculator(entrada)