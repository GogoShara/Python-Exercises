print ("Vamos jogar um jogo de viagem! \n FUI À PRAIA!")
obj= ''
praia=[]
jogar= 'y'
while jogar =='y':
    obj=input("Digite seu item que quer levar à praia: ")
    praia.append(obj)
    print (praia)
    jogar= input("Deseja colocar mais um item? Digite 'y' ou 'n' ")
    if jogar=='y':
        print("")
    else: print("O jogo acabou, eis sua lista: ", praia)
    
    
    

