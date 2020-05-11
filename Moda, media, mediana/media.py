#media , mediana e moda

def media(lista):
    media = sum(lista)/float(len(lista))
    return media

def mediana(lista):
    lista_ordenada = sorted(lista)
    t = len(lista_ordenada) #recebe o tamanho da lista

    if t % 2 == 0:
        mediana = (lista_ordenada[int(t/2)-1] + lista_ordenada[int(t/2)])/2 #se o tamanho da lista for par, a mediana será a media entre os dois numeros do meio da lista ordenada.
    elif t % 2 == 1:
        mediana = lista_ordenada[int(t/2)] #se a lista for impar, a mediana será o numero que estiver no meio do array, fazemos isso arredondando para inteiro, puxando o valor float para baixo.

    return mediana

def moda(lista):

    moda_lista = []
    lista_dic = {}

    for l in lista:
        if l not in lista_dic:
            lista_dic[l] = 1
        else:
            lista_dic[l] += 1

    maior_repeticao = max(lista_dic.values())

    if maior_repeticao > 1: #comparação para verificar a existencia de moda.
        for i in lista_dic:
            if lista_dic[i] == maior_repeticao:
                moda = i
                moda_lista.append(moda) #lista feita para o programa mostrar mais de uma moda
    else:
        moda_lista = "Essa lista não possui moda portando é amodal."

    return moda_lista
