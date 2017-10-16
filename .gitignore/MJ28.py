#Makeda Joseph
#03/15/2017


import matplotlib.pyplot as plt

import pandas as pd

pop = pd.read_csv('nycHistPop.csv',skiprows=5)

print(pop)

pop.plot.bar(x="Year")

plt.show()
