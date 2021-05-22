import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import warnings
import pickle

warnings.filterwarnings("ignore")

datos = pd.read_csv('Forest_fire.csv')
datos = np.array(datos)

X = datos[1:, 1:-1]
"""
1:-1 hacemos una especie de strip() con la celda del archivo ya que mostramos oxigeno,temperatura,humedad, ya que si no ponemos 
el -1 lo tomaria que el 0 empezaría desde la derecha y añadiría una celda mas que es ocurrencias de incendios.

el valor 1: empieza en la parte de arriba, la primara fila de izquierda a derecha, es decir, 40 45 20

"""

y = datos[1:, -1]


y = y.astype('int')
X = X.astype('int')

print(X)
print("\n-------\n")
print(y)

X_ent, X_test, y_ent, y_test = train_test_split(X,y, test_size=0.3, random_state=0)
log_reg= LogisticRegression()

log_reg.fit(X_test,y_test)
entrada= [int(x) for x in "45 32 60".split(' ')]
final= [np.array(entrada)]

b = log_reg.predict_log_proba(final)

pickle.dump(log_reg,open('model.pkl','wb'))
model=pickle.load(open('model.pkl','rb'))