#Sintaxe de uma funcção com parametros:
def funcao_com_parametro(nome_parametro):
    print(f"{nome_parametro}")
    
def funcao2_com_parametro(n1, n2, n3):
    print(f"{n1}, {n2}, {n3}")
    
# Chamar uma função com parametros:
funcao_com_parametro("Funçõe sem Python")
funcao2_com_parametro(10, 1.88, -54 )

# Chamar uma função com argumento (Envio de outro tipo de valores):
funcao_com_parametro("a")
funcao_com_parametro(10)
funcao_com_parametro(True)
funcao_com_parametro([50, 30, 57])
funcao_com_parametro({18, 1.33})

# Utilizando o *args - Permite o envio de n valores como parametros, caso você não saiba a quantidade:
def funcao_com_parametros(*valores):
    print(valores)
    print(type(valores))
    
funcao_com_parametros(10, 11, 12, 98.9)
funcao_com_parametros(2, 4, 5)
funcao_com_parametros(34)

# Função com parametros nomeados com quatidade definida -> key -> args:
def imprimir_dados(idade, nome, altura):
    print(f"A pessoa de nome {nome} possui altura de {altura} e tem {idade} anos de idade!")
    
nome = input("Digite o seu nome:")
idade = int(input("Digite a sua idade: "))
altura = float(input("Digite sua altura: "))

imprimir_dados(nome = nome, idade = idade, altura = altura)