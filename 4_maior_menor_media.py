#Função que retorna o número máximo/mínimo da lista 
def f_max_min(lista):
    return max(lista), min(lista)

#Função que calcula a média
def f_media(lista):
    return (n1 + n2 + n3 + n4 + n5) / 5

def main():
    #Entrada dos Dados
    n1 = int(input(""))
    n2 = int(input(""))
    n3 = int(input(""))
    n4 = int(input(""))
    n5 = int(input(""))
    lista = [n1, n2, n3, n4, n5]
    
    #Executa as funções
    f_max_min(lista)
    f_media(lista)
    
    #Atribui o valor das funções às variáveis
    maximo, minimo = f_max_min(lista)
    media = f_media(lista)
    
    #Mostra o resultado na tela
    print(maximo)
    print(minimo)
    print(media)

if __name__ == '__main__':
    main()

