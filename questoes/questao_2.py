## QUESTÃO 2 ##
# Escreva um programa que converta uma temperatura digitada em °C (graus celsius) 
# para °F (graus fahrenheit). 
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    # tc = Temperatura em celsius f = Fahreinheit #
    tc = float(input('Informe a temperatura em ºC: '))
    f = ((9*tc)/5)+32
    print('A temperatura de {:.1f}ºC é igual a {:.1f}ºF'.format(tc, f))
 



if __name__ == '__main__':
    main()
