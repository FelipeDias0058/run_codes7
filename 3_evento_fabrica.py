#Cria uma função para transformar segundos em 
#horas, minutos, segundos
def hora_completa(segundos):
    h = (segundos // 3600)
    m = ((segundos - (h * 3600)) // 60) 
    s = (segundos % 60)
    return h, m, s

def main():
    #Digita os segundos
    segundos = int(input(""))
    #Atribui valores da função às variáveis "hs, ms, sg"
    hs, ms, sg = hora_completa(segundos)
    #Exibe a hora completa na tela, formatada
    print(f'{hs}:{ms}:{sg}')

if __name__ == '__main__':
    main()