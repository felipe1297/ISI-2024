# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QDcx_Atm8N3TlAy3OcDXNOWgzG8UjT1X

# Final proyect
## Felipe Riaño

#### Dependencias comunes

> pip install numpy pandas matplotlib seaborn scikit-learn xgboost
"""

# Manejo de datos
import numpy as np
import pandas as pd
import scipy.stats as stats
import os
import pandas as pd
from datetime import datetime

# Visualización
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display
import plotly.express as px

# Preprocesamiento y modelos
from sklearn.model_selection import train_test_split, GridSearchCV, RandomizedSearchCV
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# XGBoost
import xgboost as xgb

# Ignorar warnings
import warnings
warnings.filterwarnings('ignore')

# Definir las rutas de los archivos
train_path = 'train.csv'
test_path = 'test.csv'

# Cargar los archivos CSV en DataFrames
train_df = pd.read_csv(train_path)
test_df = pd.read_csv(test_path)

# Mostrar las primeras filas de los DataFrames para verificar la carga
print("Train:")
display(train_df.head(5))

print("\nTest:")
display(test_df.head(5))

rendimiento_values = train_df['RENDIMIENTO_GLOBAL'].unique()
print("Valores únicos en la columna RENDIMIENTO_GLOBAL:", rendimiento_values)

# Eliminar la columna ID
train_df = train_df.drop(columns=['ID'])
test_df = test_df.drop(columns=['ID'])

are_equal = train_df['FAMI_TIENEINTERNET.1'].equals(train_df['FAMI_TIENEINTERNET'])
are_equal_test = test_df['FAMI_TIENEINTERNET.1'].equals(test_df['FAMI_TIENEINTERNET'])

print("Las columnas son iguales y tienen el mismo orden:", are_equal)
print("Las columnas son iguales y tienen el mismo orden are_equal_test:", are_equal_test)

if are_equal:
  train_df = train_df.drop(columns=['FAMI_TIENEINTERNET.1'])

if are_equal_test:
  test_df = test_df.drop(columns=['FAMI_TIENEINTERNET.1'])

"""# Relacion de columnas

### ESTU_PRGM_ACADEMICO
Interviene por su disparidad
"""

plt.figure(figsize=(200, 8))  # Ajustar el ancho de la imagen
sns.countplot(x='ESTU_PRGM_ACADEMICO', hue='RENDIMIENTO_GLOBAL', data=train_df)
plt.title('Relación entre ESTU_PRGM_ACADEMICO y RENDIMIENTO_GLOBAL')
plt.xticks(rotation=90)
plt.legend(title='RENDIMIENTO_GLOBAL')
plt.show()

"""## ESTU_PRGM_DEPARTAMENTO

Interviene por su disparidad
"""

plt.figure(figsize=(20, 8))  # Ajustar el ancho de la imagen
sns.countplot(x='ESTU_PRGM_DEPARTAMENTO', hue='RENDIMIENTO_GLOBAL', data=train_df)
plt.title('Relación entre ESTU_PRGM_DEPARTAMENTO y RENDIMIENTO_GLOBAL')
plt.xticks(rotation=90)
plt.legend(title='RENDIMIENTO_GLOBAL')
plt.show()

"""## ESTU_VALORMATRICULAUNIVERSIDAD

Interviene por su disparidad
"""

plt.figure(figsize=(20, 8))  # Ajustar el ancho de la imagen
sns.countplot(x='ESTU_VALORMATRICULAUNIVERSIDAD', hue='RENDIMIENTO_GLOBAL', data=train_df)
plt.title('Relación entre ESTU_VALORMATRICULAUNIVERSIDAD y RENDIMIENTO_GLOBAL')
plt.xticks(rotation=90)
plt.legend(title='RENDIMIENTO_GLOBAL')
plt.show()

"""## FAMI_ESTRATOVIVIENDA
interviene por su disparidad
"""

plt.figure(figsize=(20, 8))  # Ajustar el ancho de la imagen
sns.countplot(x='FAMI_ESTRATOVIVIENDA', hue='RENDIMIENTO_GLOBAL', data=train_df)
plt.title('Relación entre FAMI_ESTRATOVIVIENDA y RENDIMIENTO_GLOBAL')
plt.xticks(rotation=90)
plt.legend(title='RENDIMIENTO_GLOBAL')
plt.show()

"""## FAMI_EDUCACIONPADRE
interviene por su disparidad
"""

plt.figure(figsize=(20, 8))  # Ajustar el ancho de la imagen
sns.countplot(x='FAMI_EDUCACIONPADRE', hue='RENDIMIENTO_GLOBAL', data=train_df)
plt.title('Relación entre FAMI_EDUCACIONPADRE y RENDIMIENTO_GLOBAL')
plt.xticks(rotation=90)
plt.legend(title='RENDIMIENTO_GLOBAL')
plt.show()

"""## FAMI_EDUCACIONMADRE
interviene por su disparidad
"""

plt.figure(figsize=(20, 8))  # Ajustar el ancho de la imagen
sns.countplot(x='FAMI_EDUCACIONMADRE', hue='RENDIMIENTO_GLOBAL', data=train_df)
plt.title('Relación entre FAMI_EDUCACIONMADRE y RENDIMIENTO_GLOBAL')
plt.xticks(rotation=90)
plt.legend(title='RENDIMIENTO_GLOBAL')
plt.show()

"""## ESTU_HORASSEMANATRABAJA
interviene por su disparidad
"""

plt.figure(figsize=(20, 8))
sns.countplot(x='ESTU_HORASSEMANATRABAJA', hue='RENDIMIENTO_GLOBAL', data=train_df)
plt.title('Relación entre ESTU_HORASSEMANATRABAJA y RENDIMIENTO_GLOBAL')
plt.xticks(rotation=90)
plt.legend(title='RENDIMIENTO_GLOBAL')
plt.show()

"""## FAMI_TIENEINTERNET
interviene por su disparidad
"""

plt.figure(figsize=(20, 8))
sns.countplot(x='FAMI_TIENEINTERNET', hue='RENDIMIENTO_GLOBAL', data=train_df)
plt.title('Relación entre FAMI_TIENEINTERNET y RENDIMIENTO_GLOBAL')
plt.xticks(rotation=90)
plt.legend(title='RENDIMIENTO_GLOBAL')
plt.show()

"""## FAMI_TIENELAVADORA
interviene por su disparidad
"""

plt.figure(figsize=(20, 8))
sns.countplot(x='FAMI_TIENELAVADORA', hue='RENDIMIENTO_GLOBAL', data=train_df)
plt.title('Relación entre FAMI_TIENELAVADORA y RENDIMIENTO_GLOBAL')
plt.xticks(rotation=90)
plt.legend(title='RENDIMIENTO_GLOBAL')
plt.show()

"""## FAMI_TIENEAUTOMOVIL
p-valor es extremadamente bajo, interviene en el entrenamiento
"""

plt.figure(figsize=(20, 8))
sns.countplot(x='FAMI_TIENEAUTOMOVIL', hue='RENDIMIENTO_GLOBAL', data=train_df)
plt.title('Relación entre FAMI_TIENEAUTOMOVIL y RENDIMIENTO_GLOBAL')
plt.xticks(rotation=90)
plt.legend(title='RENDIMIENTO_GLOBAL')
plt.show()

contingency_table = pd.crosstab(train_df['FAMI_TIENEAUTOMOVIL'], train_df['RENDIMIENTO_GLOBAL'])

print(contingency_table)

chi2, p, dof, expected = stats.chi2_contingency(contingency_table)

print(f"Chi-cuadrado: {chi2}")
print(f"p-valor: {p}")
print(f"Grados de libertad: {dof}")
print("Frecuencias esperadas:")
print(expected)

alpha = 0.05
if p < alpha:
    print("La relación entre FAMI_TIENEAUTOMOVIL y RENDIMIENTO_GLOBAL es estadísticamente significativa.")
else:
    print("No se encontró una relación estadísticamente significativa entre FAMI_TIENEAUTOMOVIL y RENDIMIENTO_GLOBAL.")

"""## ESTU_PRIVADO_LIBERTAD
No se incluye debido a su falta de variabilidad y la baja representatividad de la categoría S
"""

# Verificar valores nulos
print("Nulos: ", train_df['ESTU_PRIVADO_LIBERTAD'].isnull().sum())

not_free_counts = train_df['ESTU_PRIVADO_LIBERTAD'].value_counts()
print("Cantidad por valores únicos en la columna ESTU_PRIVADO_LIBERTAD:")
print(not_free_counts)


contingency_table_no_free = pd.crosstab(train_df['ESTU_PRIVADO_LIBERTAD'], train_df['RENDIMIENTO_GLOBAL'])

print(contingency_table_no_free)

chi2_no_free, p_no_free, dof_no_free, expected_no_free = stats.chi2_contingency(contingency_table_no_free)

print(f"Chi-cuadrado: {chi2_no_free}")
print(f"p-valor: {p_no_free}")
print(f"Grados de libertad: {dof_no_free}")
print("Frecuencias esperadas:")
print(expected_no_free)

alpha = 0.05
if p_no_free < alpha:
    print("La relación entre ESTU_PRIVADO_LIBERTAD y RENDIMIENTO_GLOBAL es estadísticamente significativa.")
else:
    print("No se encontró una relación estadísticamente significativa entre ESTU_PRIVADO_LIBERTAD y RENDIMIENTO_GLOBAL.")

plt.figure(figsize=(20, 8))
sns.countplot(x='ESTU_PRIVADO_LIBERTAD', hue='RENDIMIENTO_GLOBAL', data=train_df)
plt.title('Relación entre ESTU_PRIVADO_LIBERTAD y RENDIMIENTO_GLOBAL')
plt.xticks(rotation=90)
plt.legend(title='RENDIMIENTO_GLOBAL')
plt.show()

"""## ESTU_PAGOMATRICULAPROPIO
Interviene en el entremnamiento
"""

contingency_table_pago_propio = pd.crosstab(train_df['ESTU_PAGOMATRICULAPROPIO'], train_df['RENDIMIENTO_GLOBAL'])

print(contingency_table_pago_propio)

chi2_pago_propio, p_pago_propio, dof_pago_propio, expected_pago_propio = stats.chi2_contingency(contingency_table_pago_propio)

print(f"Chi-cuadrado: {chi2_pago_propio}")
print(f"p-valor: {p_pago_propio}")
print(f"Grados de libertad: {dof_pago_propio}")
print("Frecuencias esperadas:")
print(expected_pago_propio)

alpha = 0.05
if p_pago_propio < alpha:
    print("La relación entre ESTU_PAGOMATRICULAPROPIO y RENDIMIENTO_GLOBAL es estadísticamente significativa.")
else:
    print("No se encontró una relación estadísticamente significativa entre ESTU_PAGOMATRICULAPROPIO y RENDIMIENTO_GLOBAL.")

plt.figure(figsize=(20, 8))
sns.countplot(x='ESTU_PAGOMATRICULAPROPIO', hue='RENDIMIENTO_GLOBAL', data=train_df)
plt.title('Relación entre ESTU_PAGOMATRICULAPROPIO y RENDIMIENTO_GLOBAL')
plt.xticks(rotation=90)
plt.legend(title='RENDIMIENTO_GLOBAL')
plt.show()

"""## FAMI_TIENECOMPUTADOR
Se debe incluir
"""

contingency_table_pc = pd.crosstab(train_df['FAMI_TIENECOMPUTADOR'], train_df['RENDIMIENTO_GLOBAL'])

print(contingency_table_pc)

chi2_pc , p_pc , dof_pc , expected_pc = stats.chi2_contingency(contingency_table_pc)

print(f"Chi-cuadrado: {chi2_pc}")
print(f"p-valor: {p_pc}")
print(f"Grados de libertad: {dof_pc}")
print("Frecuencias esperadas:")
print(expected_pc)

alpha = 0.05
if p_pc < alpha:
    print("La relación entre FAMI_TIENECOMPUTADOR y RENDIMIENTO_GLOBAL es estadísticamente significativa.")
else:
    print("No se encontró una relación estadísticamente significativa entre FAMI_TIENECOMPUTADOR y RENDIMIENTO_GLOBAL.")

plt.figure(figsize=(20, 8))
sns.countplot(x='FAMI_TIENECOMPUTADOR', hue='RENDIMIENTO_GLOBAL', data=train_df)
plt.title('Relación entre FAMI_TIENECOMPUTADOR y RENDIMIENTO_GLOBAL')
plt.xticks(rotation=90)
plt.legend(title='RENDIMIENTO_GLOBAL')
plt.show()

"""## PERIODO
Puede tener o no intervencion, habria que probar
"""

rendimiento_values = train_df['PERIODO'].unique()
print("Valores únicos en la columna RENDIMIENTO_GLOBAL:", rendimiento_values)

plt.figure(figsize=(100, 8))
sns.scatterplot(x='PERIODO', y='RENDIMIENTO_GLOBAL', data=train_df)
plt.title('Relación entre PERIODO y RENDIMIENTO_GLOBAL')
plt.xticks(rotation=45)
plt.show()

train_df_period_to_plot = train_df.copy()

train_df_period_to_plot['RENDIMIENTO_GLOBAL'] = train_df_period_to_plot['RENDIMIENTO_GLOBAL'].astype('category').cat.codes
plt.figure(figsize=(50, 6))
plt.hexbin(train_df_period_to_plot['PERIODO'], train_df_period_to_plot['RENDIMIENTO_GLOBAL'], gridsize=50, cmap='viridis', mincnt=1)
plt.colorbar(label='Número de puntos')
plt.xlabel('PERIODO')
plt.ylabel('RENDIMIENTO_GLOBAL')
plt.title('Relación entre PERIODO y RENDIMIENTO_GLOBAL (Hexbin Plot)')
plt.xticks(rotation=45)
plt.show()

# Eliminar la columna ESTU_PRIVADO_LIBERTAD
train_df = train_df.drop(columns=['ESTU_PRIVADO_LIBERTAD'])
test_df = test_df.drop(columns=['ESTU_PRIVADO_LIBERTAD'])

print("Train:")
display(train_df.head(5))

print("\nTest:")
display(test_df.head(5))

# Separar la columna objetivo y las características
y = train_df['RENDIMIENTO_GLOBAL']
X = train_df.drop(columns=['RENDIMIENTO_GLOBAL'])

# Verificar valores nulos en las características
print("Valores nulos en las características:")
print(X.isnull().sum())

# Verificar valores nulos en la columna objetivo
print("\nValores nulos en la columna objetivo:")
print(y.isnull().sum())

# Dividir los datos en entrenamiento + validación y prueba
X_train_val, X_test, y_train_val, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

# Dividir los datos de entrenamiento + validación en entrenamiento y validación
X_train, X_val, y_train, y_val = train_test_split(X_train_val, y_train_val, test_size=0.25, stratify=y_train_val, random_state=42)

# Mostrar el tamaño de cada conjunto
print("Tamaño del conjunto de entrenamiento:", X_train.shape)
print("Tamaño del conjunto de validación:", X_val.shape)
print("Tamaño del conjunto de prueba:", X_test.shape)

# Definir una función para manejar los valores nulos
def handle_missing_values(dataframe, strategy='mean'):
    if strategy == 'mean':
        # Rellenar con la media
        for column in dataframe.columns:
            if dataframe[column].dtype in ['int64', 'float64']:
                dataframe[column].fillna(dataframe[column].mean(), inplace=True)
            else:
                dataframe[column].fillna(dataframe[column].mode()[0], inplace=True)
    elif strategy == 'median':
        # Rellenar con la mediana
        for column in dataframe.columns:
            if dataframe[column].dtype in ['int64', 'float64']:
                dataframe[column].fillna(dataframe[column].median(), inplace=True)
            else:
                dataframe[column].fillna(dataframe[column].mode()[0], inplace=True)
    elif strategy == 'mode':
        # Rellenar con la moda
        for column in dataframe.columns:
            dataframe[column].fillna(dataframe[column].mode()[0], inplace=True)
    elif strategy == 'drop':
        # Eliminar filas con valores nulos
        dataframe.dropna(inplace=True)
    return dataframe

# Manejar valores nulos en cada conjunto
X_train = handle_missing_values(X_train, strategy='mode')
X_val = handle_missing_values(X_val, strategy='mode')
X_test = handle_missing_values(X_test, strategy='mode')

from sklearn.preprocessing import LabelEncoder

# One-Hot Encoding
X_train_onehot = pd.get_dummies(X_train, drop_first=True)
X_val_onehot = pd.get_dummies(X_val, drop_first=True)
X_test_onehot = pd.get_dummies(X_test, drop_first=True)

# Dummy Encoding
X_train_dummy = pd.get_dummies(X_train, drop_first=True)
X_val_dummy = pd.get_dummies(X_val, drop_first=True)
X_test_dummy = pd.get_dummies(X_test, drop_first=True)

X_train_onehot.info()

def save_submission(predictions, model_name):
    # Crear la carpeta 'submissions' si no existe
    if not os.path.exists('submissions'):
        os.makedirs('submissions')

    # Crear el nombre del archivo
    date_str = datetime.now().strftime('%Y-%m-%d')
    filename = f'submission_{model_name}_{date_str}.csv'
    file_path = os.path.join('submissions', filename)

    # Crear el DataFrame para las predicciones
    submission_df = pd.DataFrame({
        'ID': X_test.index,  # Asegúrate de que el índice de X_test sea el ID de los estudiantes
        'RENDIMIENTO_GLOBAL': predictions
    })

    # Guardar el archivo CSV, sobrescribiendo si ya existe
    submission_df.to_csv(file_path, index=False)
    print(f'Submission saved to {file_path}')