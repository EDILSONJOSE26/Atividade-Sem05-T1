valor_produto = int(input())
preço = valor_produto - (valor_produto * 9 / 100)
preço_5x  = valor_produto / 5
preço_10x = (valor_produto / 10) * 117 / 100
print(f'%4.2f'%preço)
print(f'%4.2f'%preço_5x)
print(f'%4.2f'%preço_10x)
