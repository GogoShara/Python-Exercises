print("Bem vindo ao seu cálculo de notas personalizado ihih")
nome=input("Digite o seu nome para começarmos: ")
print("Aluno " + nome)
materias=int(input("Quantas matérias voce terá esse semestre? "))
notas=0
soma=0
while(materias > notas):
    print("Matéria ",notas + 1)
    soma= soma + int(input("Digite a nota: "))
    notas = notas + 1
     
e=soma/materias
if(e >= 8):
    print("Você está aprovado e sua média é: " + str(e))
else:
    print("Você está reprovado e sua média é: " + str(e))
    
input("\nPressione enter para sair")
