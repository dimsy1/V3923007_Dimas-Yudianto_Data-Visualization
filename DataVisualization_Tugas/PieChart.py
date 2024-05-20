import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("Data/Data Sales3.csv", sep=";")

data['Profit'] = data['Profit'].replace('[\\$,]', '', regex=True).astype(float)

profitCategory = data.groupby('Category')['Profit'].sum()

# Membuat pie chart
plt.figure(figsize=(15, 8))
plt.pie(profitCategory, labels=profitCategory.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribusi Penjualan berdasarkan Kategori Produk')

# Menampilkan pie chart
plt.axis('equal')
plt.show()
