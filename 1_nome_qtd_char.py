#Função que mostra a quantidade de caracteres digitados
def f_qtd_char(txt):
    print(len(txt))

def main():
    #Entrada de Dados
    txt = input("")
    #Chama a execução da função
    f_qtd_char(txt)

if __name__ == '__main__':
    main()