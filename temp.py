# ces librairies devraient suffir à réaliser ce premier devoir, vous pouvez évidemment en utiliser d'autres (à importer dans cette cellule).
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# initialisation de la dataframe (à remplir)
idx = ['10th', '20th', '30th']
var = ['fixed acidity', 'pH', 'alcohol']
df_q1_1 = pd.DataFrame(np.zeros((3,3)), idx, var)
print(df_q1_1)

# chargement du dataset
data = pd.read_csv("data/math0487_fa22_hw1_data.csv")
for i in range(3):
    df_q1_1['fixed acidity'][i] = data['fixed acidity'][10*(i+1)]
    df_q1_1['pH'][i] = data['pH'][10*(i+1)]
    df_q1_1['alcohol'][i] = data['alcohol'][10*(i+1)]

# calcul des valeurs demandées


# visualisation de la dataframe
print(df_q1_1)

# initialisation de la dataframe (à remplir)
var = ['fixed acidity', 'pH', 'alcohol']
idx = ['mean', 'std', 'median', 'q25', 'q75']
df_q1_2 = pd.DataFrame(np.zeros((5,3)), idx, var)

# calcul des valeurs demandées
for colonne in var:
    df_q1_2[colonne]['mean'] = data[colonne].mean()
    df_q1_2[colonne]['std'] = data[colonne].std()
    df_q1_2[colonne]['median'] = data[colonne].median()
    df_q1_2[colonne]['q25'] = data[colonne].quantile(0.25)
    df_q1_2[colonne]['q75'] = data[colonne].quantile(0.75)


# visualisation de la dataframe
print(df_q1_2)

plt.subplot()
plt.boxplot(data['fixed acidity'], showmeans=True)
plt.title('fixed acidity')

plt.figure()
plt.boxplot(data['pH'], showmeans=True)
plt.title('pH')

plt.figure()
plt.boxplot(data['alcohol'], showmeans=True)
plt.title('alcohol')





