#ex36Mundo2
#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.Pergunte o 
#valor da casa , o saláriodo compradore em quantos anos ele vai pagar.
#A prestação mensal , não pode exceder 30% do salário ou então o empréstimo será negado.

def linha():
    print('Controle de Terrenos')
    print('-=-'*10)





def Prestação(Casa , Salario , Anos ,):

    Total = Casa / ( Anos * 12)
    Mínimo = Salario * 0.3
    print('Para pagar uma casa de R$ {} em {} anos'.format(Casa, Anos))
    if Total <= Mínimo  :
        linha()
        print('Emprestimo NEGADO , a prestação no valor de {} excede os 30 por cento do seu salario {}'.format(Total , Mínimo))
    else :
        print(f'Emprestimo CONCEDIDO !! , o valor da prestação é {Total}') 








    






#Programa Principal:
Casa = float(input('Digite o valor da Casa'))
Salario = float(input('Digite o seu salário'))
Anos = int(input('Quantos de financiamento'))


Prestação(Casa , Salario , Anos)
