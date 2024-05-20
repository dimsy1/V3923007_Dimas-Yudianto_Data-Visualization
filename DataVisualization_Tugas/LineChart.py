import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("Data/Data Sales3.csv", sep=";")

# Mengubah format kolom Sales dan Profit menjadi float
data['Profit'] = data['Profit'].replace('[\\$,]', '', regex=True).astype(float)

data['Year'] = pd.to_datetime(data['Year'], format='%Y').dt.year

# Group sesuai tahun dan menjumlahkan kolom profit
profit_tahunan = data.groupby('Year')['Profit'].sum()

plt.figure(figsize=(10, 6))
plt.plot(profit_tahunan.index, profit_tahunan.values, marker='o')
plt.title('Total Profit per Tahun')
plt.xlabel('Tahun')
plt.ylabel('Total Profit ($)')
plt.grid(True)
plt.xticks(profit_tahunan.index)
plt.tight_layout()
plt.show()
