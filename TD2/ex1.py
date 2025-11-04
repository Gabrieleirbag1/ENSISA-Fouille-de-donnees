import numpy as np
import pandas as pd
import seaborn as sns

# question 1.1
df = pd.read_csv('http://germain-forestier.info/dataset/herbicide.csv', index_col='ID')

pourcentage_survivants = (df['nb_plants_survivants'] / df['nb_plants']) * 100
df['pourcentage_survivants'] = pourcentage_survivants

# question 1.2
print(df.info())
print(df.head())

# question 1.3
print("Moyenne", np.mean(df['nb_plants']))
print("Variance", np.var(df['nb_plants']))
print("Ecart type", np.std(df['nb_plants']))
print("Max", np.max(df['nb_plants']))
print("Min", np.min(df['nb_plants']))


# question 1.4
# print(len(df[df['pourcentage_survivants'] < 5]))
print(df[df['pourcentage_survivants'] < 5].head())

# question 1.5
temoin = df[df['herbicide'].str.contains('aucun')]
print("Témoin", temoin)

# question 1.6
moyenne_survivants_temoin = np.mean(temoin['pourcentage_survivants'])
print("Moyenne survivants témoin", moyenne_survivants_temoin)
ecarts_type_temoin = np.std(temoin['pourcentage_survivants'])
print("Ecart type témoin", ecarts_type_temoin, "\n")
seuil = moyenne_survivants_temoin + 2 * ecarts_type_temoin

# question 1.7

plantes = df['herbicide'].unique()
for herbicide in plantes:
    subset = df[df['herbicide'] == herbicide]
    moyenne = np.mean(subset['pourcentage_survivants'])
    ecart_type = np.std(subset['pourcentage_survivants'])
    print(f"Herbicide: {herbicide}, Moyenne: {moyenne}, Ecart type: {ecart_type}\n")

# question 1.8
plante_list = df['plante'].unique()

for p in plante_list:
    print('Resultat pour ['+p+']')
    subset = df[df['plante'] == p]
    print('mean: '+str(np.mean(subset['pourcentage_survivants'])))
    print('std: '+str(np.std(subset['pourcentage_survivants'])))
    print('')

# question 1.9
import matplotlib.pyplot as plt
plt.hist(df['pourcentage_survivants'], bins=30)
plt.title('Histogramme du pourcentage de survivants')
plt.xlabel('Pourcentage de survivants')
plt.ylabel('Fréquence')
plt.show()

# question 1.10
plantes = df['plante'].unique()
labels = []
for plante in plantes:
    labels.append(plante)
plt.pie(df["plante"].value_counts(), labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('Répartition du nombre de plantes par type de plante')
plt.show()

# question 1.11
crop=[]
for plante in plantes:
    crop.append((df[df['plante'] == plante]["nb_plants_survivants"]))
plt.boxplot(crop)
plt.xticks([1,2,3],plantes)
plt.plot()
plt.show()

# question 1.12
herbicides = df['herbicide'].unique()
herbicides = np.setdiff1d(herbicides, ["aucun"])

crop=[]
for herbicide in herbicides:
    crop.append((df[df['herbicide'] == herbicide]["nb_plants_survivants"]))
plt.boxplot(crop)
plt.xticks([1,2,3],herbicides)
plt.plot()
plt.show()

# question 1.13

plantes = df["plante"]
survivants = df["nb_plants_survivants"]
herbicide = df["herbicide"]
sns.stripplot(x=plantes, y=survivants, hue=herbicide, data=df, dodge=True)
plt.show()

# question 1.14
df_sansTemoin = df[df['herbicide'] != 'aucun']
print(df_sansTemoin)
