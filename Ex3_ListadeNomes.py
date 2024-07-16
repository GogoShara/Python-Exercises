print ("Vamos armazenar os nomes dos seus mais queridos!!")
entrys= ''
qn=0
nome=[]
while(qn < 5):
    print("Nome ",qn+1)
    entrys = entrys + input("Digite o Nome: ")
    nome.append(entrys)
    qn = qn + 1
print (nome)
