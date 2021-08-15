'''Como exercício prático, tente escrever um programa para calcular e informar o IMC (índice de massa corpórea) do usuário, que deverá fornecer seu peso e sua altura. Lembre-se que o IMC é calculado pela fórmula:
 IMC= peso/ altura²'''

peso = eval(input("Digite seu peso"))
altura = eval(input("Digite sua altura"))
IMC = peso / altura**2
print("Seu IMC é:", IMC)

