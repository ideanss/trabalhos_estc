saida = ''
def adicao(num1, num2):
    return num1 + num2
def subtracao(num1, num2):
    return num1 - num2
def multiplicacao(num1, num2):
    return num1 * num2
def divisao(num1, num2):
    if num1 or num2 == 0:
        print("Não foi possivel realizar a divisão por 0")
    else:
        return num1 / num2

def calculadora(num1, num2, operacao):
    if operacao == '+' or operacao.lower() == 'adicao':
        resultado = adicao(num1, num2)
    elif operacao == '-' or operacao.lower() == 'subtracao':
        resultado = subtracao(num1, num2)
    elif operacao == '*' or operacao.lower() == 'multiplicacao':
        resultado = multiplicacao(num1, num2)
    elif operacao == '/' or operacao.lower() == 'divisao':
        resultado = divisao(num1, num2)
    else:
        resultado = "Operação inválida"

    return resultado

while saida != 'n':

    num1 = float(input("Digite um valor: "))
    num2 = float(input("Digite o segundo valor: "))
    operacao = input("Digite qual operação realizar: ")

    resultado = calculadora(num1, num2, operacao)
    print('Resultado: ', resultado)

    encerrar = input("Deseja continuar? Digite S ou N: ")
    if encerrar == "S" or encerrar == "s":
        print("Calculadora encerrada")
        break