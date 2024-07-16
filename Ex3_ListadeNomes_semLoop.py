print ("Vamos armazenar os nomes dos seus mais queridos!!")
n1=input("'Digite o primeiro nome: ")
n2=input("'Digite o segundo nome: ")
n3=input("'Digite o terceiro nome: ")
n4=input("'Digite o quarto nome: ")
n5=input("'Digite o quinto nome: ")
n= [n1, n2 , n3 , n4 , n5]
print ('A lista de nomes: ', *n, sep= '\n-')
