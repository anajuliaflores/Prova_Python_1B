# Função para calcular o IMC
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

# Função para classificar o IMC segundo a tabela da OMS
def classificar_imc(imc):
    if imc < 17:
        return "Muito abaixo do peso"
    elif 17 <= imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    elif 30 <= imc < 35:
        return "Obesidade Grau I"
    elif 35 <= imc < 40:
        return "Obesidade Grau II"
    else:
        return "Obesidade Grau III"

# Entrada de dados
peso = float(input("Informe seu peso (kg): "))
altura = float(input("Informe sua altura (m): "))

# Cálculo do IMC
imc = calcular_imc(peso, altura)

# Exibição do resultado
print(f"Seu IMC é: {imc:.2f}")
print(f"Classificação: {classificar_imc(imc)}")

'''
quando fiz o código imaginava de devia estar bem perto, mas percebi que poderia ter melhorado em algumas partes. 
'''