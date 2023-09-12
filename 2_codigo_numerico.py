#Usa a função "ord" para exibir o codigo unicode do caractere
def f_cod_num(caractere):
    print(ord(caractere))


def main():
    #Entrada de Dados
    char_input = input("")
    #Formata a string para que apenas o primeiro 
    #caractere seja lido
    caractere = char_input[0:1]
    
    #Executa a função "f_cod_num"
    f_cod_num(caractere)

if __name__ == '__main__':
    main()