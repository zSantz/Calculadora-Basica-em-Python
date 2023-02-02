"""Calculadora"""
while True:
    num_1 = input('Digite o primeiro número: ')
    num_2 = input('Digite o segundo número: ')

    print('SOMA(+) SUBTRAÇÃO(-) DIVISÃO(/) MULTIPLICAÇÃO (x)')
    operacao = input('Digite a operação que deseja fazer: ').lower()

    try:
        num_1 = float(num_1)
        num_2 = float(num_2)
        
        if operacao == '+': # soma
                print(f'{num_1} + {num_2} = {num_1+num_2}')

        elif operacao == '-': # subtração
                print(f'{num_1} - {num_2} = {num_1-num_2}')

        elif operacao == '/': # divisão
                print(f'{num_1} / {num_2} = {num_1/num_2}')

        elif operacao == 'x': # multiplicação
                print(f'{num_1} x {num_2} = {num_1*num_2}')

        else:
                print('Operação Invalida')
                continue
    except:
        print('Um ou ambos os números digitados são invalidos')
        continue

    sair = input('Deseja continuar? ').lower().startswith('n')
    if sair:
        break
    