import matplotlib.pyplot as plt

# Dados de exemplo
idades = [15, 22, 34, 45, 52, 63, 70, 85]
categorias = ['Novo', 'Novo', 'Novo', 'Meia-idade', 'Meia-idade', 'Velho', 'Velho', 'Velho']

# Contagem de categorias
contagem = {'Novo': 0, 'Meia-idade': 0, 'Velho': 0}
for categoria in categorias:
    contagem[categoria] += 1

# Dados para o gráfico
categorias = list(contagem.keys())
quantidades = list(contagem.values())

# Criando o gráfico de barras
plt.bar(categorias, quantidades, color=['blue', 'green', 'red'])
plt.xlabel('Categoria')
plt.ylabel('Quantidade')
plt.title('Distribuição de Idades')
plt.show()
