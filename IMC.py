'''Como exercício prático, tente escrever um programa para calcular e informar o IMC (índice de massa corpórea) do usuário, que deverá fornecer seu peso e sua altura. Lembre-se que o IMC é calculado pela fórmula:
 IMC= peso/ altura²'''

while True:
    peso = float(input('Digite o seu peso: '))
    altura = float(input('Digite a sua altura em metros: '))
    imc = peso / (altura ** 2)
    print(f'O seu IMC é: {imc:.1f}.')
    if 16 > imc < 16.9:
        print('Resultado: Muito abaixo do peso.')

    elif 17 > imc < 18.4:
        print('Resultado: Abaixo do peso.')   

    elif 18.5 > imc < 24.9:
        print('Resultado: Peso normal.')

    elif 25 > imc < 29.9:
        print('Resultado: Acima do peso.')

    elif 30 > imc < 34.9:
        print('Resultado: Obesidade Grau I.')

    elif 35 > imc < 40:
        print('Resultado: Obesidade Grau II.')

    elif imc > 40:
        print('Resultado: Obesidade Grau III.')

    saída = input('Você deseja calcular novamente? [S/N]: ').strip().upper()[0]
    if 'N' in saída:
        break
