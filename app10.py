print("Calculadora simples") 

opcao=int(input("voce deseja 1-soma 2-subtração 3-multiplicação 4-divisão"))

if opcao == 1:
   num5=int(input("Digite o primeiro numero"))
   num6=int(input("Digite o segundo numero"))
   som= num5+num6
   print(f"resultado da soma de numero{num5}+ {num6}={som}")
elif opcao==2:
   num5=int(input("Digite o primeiro numero"))
   num6=int(input("Digite o segundo numero"))
   som= num5-num6
   print(f"resultado da soma de numero{num5}-{num6}={som}")
elif opcao==3:
   num5=int(input("Digite o primeiro numero"))
   num6=int(input("Digite o segundo numero"))
   som= num5*num6
   print(f"resultado da soma de numero{num5}* {num6}={som}")
elif opcao==4:
   num5=int(input("Digite o primeiro numero"))
   num6=int(input("Digite o segundo numero"))
   som= num5/num6
   print(f"resultado da soma de numero{num5}/ {num6}={som}")
  
print("##############################################################")
#Número Primo
print("Número Primo") 

numeroPrimo=int(input("Digite um numero"))