import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("Data/Data Sales3.csv", sep=";")

# Mengubah format kolom Sales dan Profit menjadi float
data['Profit'] = data['Profit'].replace('[\\$,]', '', regex=True).astype(float)

months_order = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
data['Month'] = pd.Categorical(data['Month'], categories=months_order, ordered=True)

data = data.sort_values('Month')

data['Month'] = data['Month'].astype(str)

# Buat scatter plot
plt.figure(figsize=(15, 6))
plt.scatter(data['Month'], data['Profit'], color='blue', alpha=0.5)

plt.title('Scatter Plot Profit')
plt.xlabel('Month')
plt.ylabel('Profit ($)')

plt.grid(True)
plt.show()
