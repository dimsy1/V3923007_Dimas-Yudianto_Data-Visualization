import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("Data/Data Sales3.csv", sep=";")

plt.hist(data['Quantity'])

plt.title('Histogram Quantity')

plt.show()
