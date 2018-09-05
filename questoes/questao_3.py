## QUESTÃO 3 ##
# Escreva um programa que calcule a área de um círculo, o diâmetro e o comprimento 
# da circunferência. Solicite que o usuário insira o raio e imprima uma mensagem 
# agradável de volta para o usuário com a resposta. 
##

##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    from math import pi
    # r = raio a = área d = diâmetro cc = comprimento da circunferência
    r = int(input('Digite o tamanho do raio em centímetros: '))
    a = pi * pow(r, 2)
    d = r * 2
    cc = 2 * pi * r
    print('Uma circunferência com raio igual a {} possui uma área de {:.2f} cm², um diâmetro de {:.2f} cm e um comprimento de {:.2f} cm'.format(r, a, d, cc))



    
if __name__ == '__main__':
    main()
