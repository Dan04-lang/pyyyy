print("Conversor de temperatura")
valor= int(input("fahrenheit 1 ou Celsius 2: "))

if valor == 1:
    fahrenheit = float(input("digite a temperatura em fahrenheit:"))
    celsius = (fahrenheit - 32) * 5.0/9.0
    print(f"{fahrenheit} fahrenheit é igual a {celsius} celsius")
elif valor == 2:
    celsius = float(input("digite a temperatura em celsius:"))
    fahrenheit = (celsius * 9.0/5.0) + 32
    print(f"{celsius} celsius é igual a {fahrenheit} fahrenheit")