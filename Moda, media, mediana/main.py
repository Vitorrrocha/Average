import aleatorio
import media as m

tamanho = int(input("Digite o tamanho da lista: \n"))

lista = aleatorio.geraListaInteiro(tamanho)

media = m.media(lista)
mediana = m.mediana(lista)
moda = m.moda(lista)

print(f"Minha lista é: {sorted(lista)}\n")
print(f"A media da lista é: {media:.2f}\n")
print(f"A mediana da lista é: {mediana}\n")
print(f"O valor moda é/são: {sorted(moda)}")