
def somar(a,b):
    return a + b

def exibir_boas_vindas():
    print("Bem-vindo ao sistema de cálculo de somas!")
    nome = input("Digite seu nome: ")
    print(f"Olá, {nome}! Vamos somar dois números.")

def fatorial(n):
    if n < 0:
        raise ValueError("O fatorial não está definido para números negativos.")
    elif n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado

# Exemplo de uso:
print(fatorial(5))  # Saída: 120


def para_minuscula(texto):
    """
    Recebe uma string e retorna em letras minúsculas.
    """
    return texto.lower()

# Exemplo de uso:
print(para_minuscula("Olá Mundo!"))  # saída: "olá mundo!"

if __name__ == "__main__":
    exibir_boas_vindas()
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))
    resultado = somar(a, b)
    print(f"Resultado da soma: {resultado}")


