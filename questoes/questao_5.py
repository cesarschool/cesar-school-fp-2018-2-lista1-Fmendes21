## QUESTÃO 5 ##
# Escreva um programa para calcular a redução do tempo de vida de um fumante. 
# Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. 
# Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule 
# quantos dias de vida um fumante perderá. Exiba o total em dias. 
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    # qt = quantidade total de cigarro em X anos. tvp = tempo de vida perdido em dias
    cig = int(input('Quantos cigarros você fuma por dia? '))
    anos = int(input('Você fuma a quantos anos? '))
    qt = cig*(360*anos)
    tvp = ((qt*10)/360)/24
    # dividi por 360 para saber o tempo em horas, em seguida dividi as horas obtidas por 24, para saber a quantidade de dias
    print('Levando em consideração que 1 cigarro = 10min a menos de vida \n'
      'Você já perdeu {:.1f} dias de vida'.format(tvp))


    
if __name__ == '__main__':
    main()
