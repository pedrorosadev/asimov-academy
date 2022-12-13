import os

print('='*10 + ' Calculadora ' + '='*10)

operations = {
"+": "Adição",
"-": "Subtração",
"*": "Multiplicação",
"/": "Divisão",
"**": "Exponenciação"
}

def addiction(num1, num2):
    return num1 + num2

def subtration(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

def potentiation(base, potencia):
    return base ** potencia

while True:
    os.system("clear")
    i = 0
    for operation, name in operations.items():
        print(f'{i}:{name}')
        i += 1
    operation = int(input('\nEscolha a operação que deseja realizar: \n\n>>> '))
    os.system("clear")
    operation_string = list(operations.keys())[operation]
    print(f'\n>>> {operation_string} escolhida')

    num1 = float(input('\n1º valor: \n\n>>> '))
    num2 = float(input('\n2º valor: \n\n>>> '))  

    if(operation == 0):
        result = addiction(num1, num2)
    elif(operation == 1):
        result = subtration(num1, num2)
    elif(operation == 2):
        result = multiplication(num1, num2)
    elif(operation == 3):
        result = division(num1, num2)
    elif(operation == 4):
        result = potentiation(num1, num2)
    else:
        print('\nSaindo...')
        break

    print(f'{num1} {operation_string} {num2} = {result:.2f}')
    comando = int(input("\nDeseja realizar outra operação?\n[1] Para Sair\n\n>>>"))
    if(comando == 1):
        break