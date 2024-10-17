def eh_palindromo(texto):
    texto = texto.replace(" ", "").lower()
    return texto == texto[::-1]  

texto = input("Digite uma palavra/frase: ")
if eh_palindromo(texto):
    print(f"A palavra/frase '{texto}' é um palíndromo")
else:
    print(f"A palavra/frase '{texto}' não é um palíndromo")


