lista= [4,9,0,5,6,16]
esq= 0
dire= len(lista)-1
while (esq < dire):
    ihi = lista[esq]
    lista[esq] = lista[dire]
    lista[dire] = ihi
    esq = esq + 1
    dire = dire - 1
print (lista)
input("Digite Enter para fechar")
