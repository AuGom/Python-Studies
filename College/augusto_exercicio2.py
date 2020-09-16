venda = float(input('Digite o total das vendas: '))

fixo = float(500)
comissao = float(0.06)

fat = fixo+venda*comissao
print(f'{fat:.2f}')
