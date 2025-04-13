def precedencia(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    return 0

def infix_a_postfix(expresion):
    salida = []
    pila = []
    tokens = expresion.split()

    for token in tokens:
        if token.isdigit():
            salida.append(token)
        elif token == '(':
            pila.append(token)
        elif token == ')':
            while pila and pila[-1] != '(':
                salida.append(pila.pop())
            pila.pop()
        else:
            while pila and precedencia(pila[-1]) >= precedencia(token):
                salida.append(pila.pop())
            pila.append(token)

    while pila:
        salida.append(pila.pop())

    return salida

def evaluate_postfix(postfix):
    pila = []
    for token in postfix:
        if token.isdigit():
            pila.append(int(token))
        else:
            b = pila.pop()
            a = pila.pop()
            if token == '+':
                pila.append(a + b)
            elif token == '-':
                pila.append(a - b)
            elif token == '*':
                pila.append(a * b)
            elif token == '/':
                pila.append(a / b)
    return pila[0]

def evaluate_infix(expresion):
    postfix = infix_a_postfix(expresion)
    print("Expresión en postfix:", ' '.join(map(str, postfix)))
    return evaluate_postfix(postfix)

# ejecucion
print("Resultado final:", evaluate_infix("( 3 + 4 ) * 2"))
