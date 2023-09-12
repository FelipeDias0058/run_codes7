#Cria uma função para calcular o valor com desconto
def f_desconto(valor):
    return valor * 0.91

#Função para calcular a prestação em 5 vezes
def f_prestacao5(valor):
    return valor / 5

#Função calculando a prestação em 10 vezes, com juros
def f_prestacao10(valor):
    return (valor / 10) * 1.17

def main():
    
    #Entrada do valor original
    valor = float(input(""))
    
    #Exibe os valores na tela
    print(f'{f_desconto(valor):.2f}')
    print(f'{f_prestacao5(valor):.2f}')
    print(f'{f_prestacao10(valor):.2f}')

if __name__ == '__main__':
    main()
    
