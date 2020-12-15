import matplotlib.pyplot as plt

data = {'pizza': 20, 'sushi': 15, 'minestrone': 5, 'lasagna': 10}
names = list(data.keys())
values = list(data.values())

fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=True)
axs[0].bar(names, values)
axs[1].scatter(names, values)
axs[2].plot(names, values)
fig.suptitle('Cibi preferiti di 50 ragazzi')

plt.show()
