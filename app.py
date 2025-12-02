
def soma(a,b):
    return a + b

def exibir_boas_vindas():
    print("Bem-vindo ao sistema de cálculo de somas!")
    nome = input("Digite seu nome: ")
    print(f"Olá, {nome}! Vamos somar dois números.")


if __name__ == "__main__":
    exibir_boas_vindas()
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))
    resultado = somar(a, b)
    print(f"Resultado da soma: {resultado}")
