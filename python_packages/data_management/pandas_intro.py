# %% importando el paquete pandas
import pandas as pd

# %% Cargando datos desde un archivo csv en dataframe
df = pd.read_csv('datasets/lugares-turisticos-publicos.csv')

# %% Mostrando las primeras filas del dataframe
df.head(10)

# %% Mostrando las ultimas filas del dataframe
df.tail(10)

# %% Mostrando los nombres de las columnas del dataframe
df.keys()

# %% Explorar los tipos de datos y el número de casos presentes de cada columna
df.info()

# %% Seleccionando columnas del dataframe
df[["Nombre", "Tipo", "Provincia"]]


# %% Filtrando registros del dataframe
df[(df["TipoLugar"]=="Rio") & (df["Provincia"]=="Azuay")]


# %% Analizando columnas/variables del dataframe
df['TipoLugar'].describe()


# %% Contabilizando la frecuencia de valores en las columnas/variables del dataframe
df['TipoLugar'].value_counts()
# %%