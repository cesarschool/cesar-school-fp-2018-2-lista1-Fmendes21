## QUESTÃO 1 ## 
# Faça um programa que calcule o aumento de um salário. Ele deve solicitar o 
# valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do 
# novo salário. 
##

##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    #sal = salário aum = aumento sf = salário final#
    sal = float(input('Qual é o salário do funcionário? '))
    aum = float(input('De quanto será o aumento? (Digite o valor em porcentagem) '))
    sf = sal+(sal*aum/100)
    print('O funcionário que ganhava R${:.2f}, com {:.1f}% de aumento, passará a ganhar R${:.2f}'.format(sal, aum, sf))
    
    


if __name__ == '__main__':
    main()
