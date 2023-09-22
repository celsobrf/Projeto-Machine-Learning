# -*- coding: utf-8 -*-
"""Projeto Machine Learning.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mRl-Jk0boN05zXbtPBi04gR1AFmQ7TKz
"""

import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split

df = pd.read_csv('https://celsobrf.github.io/Projeto-Machine-Learning/smoking_driking_dataset_Ver01.csv')

df

print("Shape",df.shape)
print(df.describe())

# Verificando valores faltantes
df.isna().sum()

# Verifiando linha duplicadas
df[df.duplicated].shape

# Removendo as duplicadas
df = df.drop_duplicates(keep='first')
df[df.duplicated].shape

# Devido ao tamanho do dataset, iremos trabalhar com uma amostra representativa dele (20%)
# Ao fazer as análises necessárias e fazer com que um modelo trabalhe bem em cima desse sample,
# faremos com que ele rode em cima de todos os dados e avaliaremos sua performance.

df_20 = df.sample(frac=0.2)
df_20

"""Iniciaremos com uma anáise dos dados para depois prosseguirmos com uma preparação dos dados e treinamento de um modelo"""

df.dtypes

"""Os dados de todas as colunas são do tipo numérico, com exceção da coluna `sexo` e da coluna `Bebe_SN`."""

# Renomeando colunas
df = df.rename({'SMK_stat_type_cd':'smoking_history','DRK_YN':'drinking_history'}, axis = 'columns')

# Explorando com visualizações
import matplotlib.pyplot as plt
import seaborn as sns

## Como não quero fazer nenhuma alteração no conjunto de dados original, criarei uma cópia
df_two = df.copy()

## O tipo de coluna de sexo é alterado para numérico
df_two['sex'] = df_two['sex'].map({'Male':1,'Female':2})
df_two['drinking_history'] = df_two['drinking_history']. map({'Y':1,'N':0})

# Correlação
corr_matrix = df_two.corr()

plt.figure(figsize = (15,15))
sns.set(font_scale=0.8)

sns.heatmap(corr_matrix,annot=True,cmap='coolwarm',linewidths=0.5)
plt.title('Correlation Heatmap',fontsize = 25)

# Sexo por polulação
sns.countplot(data = df, x='smoking_history',hue='sex',palette='bright')

non_smokers = df[df['smoking_history'] == 1.0]
ex_smokers = df[df['smoking_history'] == 2.0]
smokers = df[df['smoking_history'] == 3.0]

fig,axes = plt.subplots (nrows=1,ncols=3,figsize =(8,3))


axes[0].hist(non_smokers['hemoglobin'],color = 'blue')
axes[0].set_title('Non Smokers')
axes[1].hist(ex_smokers['hemoglobin'],color = 'blue')
axes[1].set_title('Ex-Smokers')
axes[2].hist(smokers['hemoglobin'],color = 'blue')
axes[2].set_title('Smokers')

# Preparando para o modelo
X=df.drop(columns=['drinking_history'],axis=1)
y = df.drinking_history

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3)

import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix ,classification_report