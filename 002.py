print("Bem vindo ao seu cálcuilo de notas personalizado ihih")
nome=input("Digite o seu nome para começarmos: ")
print("Aluno " + nome)
a= int(input("Digite sua primeira nota: "))
b= int(input("Digite sua segunda nota: "))
c= int(input("Digite sua terceira nota: "))
d= int(input("Digite sua quarta nota: "))
e=(a+b+c+d)/4
if(e >= 8):
    print("Você está aprovado e sua média é: " + str(e))
else:
    print("Você está reprovado e sua média é: " + str(e))
    
