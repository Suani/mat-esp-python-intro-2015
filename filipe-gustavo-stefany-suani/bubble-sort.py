import matplotlib.pyplot as plt
N = 20
lista = [11, 18, 3, 1, 16, 12, 6, 19, 5, 0, 14, 4, 17, 9, 13, 7, 10, 15, 2, 8]
print("lista original", lista) 
plt.figure()
plt.plot(range(0, N), lista, "ok")
plt.title("estado inicial")
plt.xlabel("indices")
plt.ylabel("valores")
plt.savefig("fig/bubble-inicio.png")
plt.close()
a=0
cont = 0
# considerando i numeros da lista comecando na posicao 0 e terminando na posicao N-1, indo de 1 a 1 
for i in range(0, N-1, 1):
# considerando j numeros da lista comecando em uma posicao a frente do i e terminando no numero da ultima posicao da lista, indo de 1 a 1
     for j in range(i + 1, N, 1):
# comparando o valor de i com j, caso i seja maior que j, entao seguir os passos seguintes
        if lista[i] > lista[j]:
            temp = lista[i]
            lista[i] = lista[j]
            lista[j] = temp
            a=a+1
            plt.figure() 
            plt.plot (range(0, N), lista, "ok")
            plt.title("bubble-troca-{}".format(a))
            plt.xlabel("indices")
            plt.ylabel("valores")
            plt.savefig("fig/bubble-troca-{}.png".format(a))
            plt.close()
        x = range(0,20,1)
        y = lista
        plt.figure()
        plt.plot(x, y, 'ok')
        plt.plot (i, lista[i], "or")
        plt.plot (j, lista[j], "ob")
        plt.title("bubble-it-{}".format(cont))
        plt.xlabel("indices")
        plt.ylabel("valores")
        plt.savefig("fig/bubble-it-{}.png".format(cont))
        cont += 1
        plt.close()
print("lista ordem crescente", lista)
plt.figure()
plt.plot (range(0, N), lista, "ok")
plt.title("estado final")
plt.xlabel("indices")
plt.ylabel("valores")
plt.savefig("fig/bubble-final.png")
plt.close()
print("cinco maiores valores", lista[N-5:N])
print("cinco menores valores", lista[0:5])
# organizando a lista com valores em ordem crescente, lista com cinco menores e 5 maiores