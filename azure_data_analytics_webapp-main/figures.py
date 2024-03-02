import plotly.express as px
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('HISTORICO-MLG-2023.csv')
consumos = ['KWH-1','KWH-2','KWH-3','KWH-4','KWH-5','KWH-6','KWH-7',
            'KWH-8','KWH-9','KWH-10']
pagos = ['FAC-1','FAC-2','FAC-3','FAC-4','FAC-5','FAC-6','FAC-7',
         'FAC-8','FAC-9','FAC-10']
df_consumos = df[consumos]
df_consumos = df[consumos]
df_pagos = df[pagos]

def bar_chart(df):
    """
    Sample Plotly Bar Chart
    """
    # Crear una figura de Plotly Bar Chart
    fig = px.bar(df, x="Category", y="Values", title="Bar Chart")
    fig.show()

    # Realizar un histograma para cada columna en el DataFrame
    for col in df.columns:
        if df[col].dtype != 'object':  # Verificar si la columna no es de tipo objeto
            plt.hist(df[col], bins=10)
            plt.xlabel(col)
            plt.ylabel("Frecuencia")
            plt.title(f"Histograma de {col}")
            plt.show()

# Crear un DataFrame de ejemplo
df = pd.DataFrame({
    "Category": ["A", "B", "C", "D", "E"],
    "Values": np.random.randint(10, 100, size=5)
})

# Llamar a la función bar_chart() con el DataFrame de ejemplo
bar_chart(df)

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

df.fillna(0, inplace=True)  # Reemplazar valores faltantes con cero por simplicidad, ajusta según tu caso

# Escalar las características
scaler = StandardScaler()
consumo_features = df[['KWH-1', 'KWH-2', 'KWH-3', 'KWH-4', 'KWH-5', 'KWH-6', 'KWH-7', 'KWH-8', 'KWH-9', 'KWH-10']]
scaled_features = scaler.fit_transform(consumo_features)

# Aplicar K-Means con 3 clusters
kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(scaled_features)
df['Cluster'] = clusters

# Visualizar los resultados del clustering
fig = px.scatter(df, x='TOTALDEUDA', y='Cluster', color='Cluster', title='Clustering de Total de Deuda según los Patrones de Consumo de Energía',
                 labels={'TOTALDEUDA': 'Total de Deuda', 'Cluster': 'Cluster'})
fig.show()