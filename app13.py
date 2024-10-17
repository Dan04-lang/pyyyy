def fatorial(n):
    if n < 0:
        return "Não é possível calcular o fatorial de um número negativo."
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

n = int(input("Digite um número: "))
print(fatorial(n))