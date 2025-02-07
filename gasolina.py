import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('gasolina.csv')
df.head()

# Criar o gráfico
plt.figure(figsize=(10, 5))
sns.lineplot(data=df, x='dia', y='venda', marker='o', color='b')


plt.title('Variação do Preço da Gasolina ao Longo dos Dias')
plt.xlabel('Dia')
plt.ylabel('Preço (R$)')
plt.grid(True)

plt.savefig('gasolina.png')
plt.show()