import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("Data/Data Sales3.csv", sep=";")

# Mengubah format kolom Sales dan Profit menjadi float
data['Profit'] = data['Profit'].replace('[\\$,]', '', regex=True).astype(float)

# Menjumlahkan profit berdasarkan kota
total_profit_per_city = data.groupby('City')['Profit'].sum().reset_index()

# Buat bar chart
plt.figure(figsize=(10, 6))
plt.bar(total_profit_per_city['City'], total_profit_per_city['Profit'], color='blue')

plt.title('Profit Penjualan berdasarkan Kota')
plt.xlabel('City')
plt.ylabel('Profit (Dalam Jutaan Dolar)')

plt.grid(True)
plt.show()
