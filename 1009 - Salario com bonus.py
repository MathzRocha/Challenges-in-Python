nome = input()
fixo = float(input())
total_vendas = float(input())
comissao = (15 * total_vendas) / 100
total = comissao + fixo

print(f'TOTAL = R$ {total:.2f}')
