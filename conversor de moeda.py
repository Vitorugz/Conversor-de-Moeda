# conversor de moedas

valor = int(input('Digite o valor a ser convertido: '))

vlr_dolar = 5.20
vlr_euro= 5.49

print('='*29)
print('|  Opções                             |')
print('|                                     |')
print('|  Converter para $ Dolar       [1]   |')
print('|  Converter para € Euro        [2]   |')
print('|  Converter Dolar para R$ Real [3]   |')
print('|  Converter Euro para R$ Real  [4]   |')
print('='*29)
opcao = int(input('Selecione uma das opções: '))

if opcao == 1:
    print(f'R${valor} convertido em Dolar é: $''%.2f' % (valor/vlr_dolar))
elif opcao == 2:
    print(f'R${valor} convertido em Euro é: €''%.2f' % (valor/vlr_euro))
elif opcao == 3:
    print(f'${valor} convertido em Real é: R$''%.2f' % (valor*vlr_dolar))
elif opcao == 4:
    print(f'€{valor} covertido em  Real é: €''%.2f' % (valor*vlr_euro))
else:
    print('Você não informou uma opção valida')



