def fibinacci(n):
    sequencia =[0, 1]
    while len(sequencia) < n:
        proximo = sequencia[-1] + sequencia[-2]
        sequencia.append(proximo)
    return sequencia[:n]

n = int(input("Digite o número de termos desejados: "))
print(fibinacci(n))