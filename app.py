from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np
from jinja2 import debug

app = Flask(__name__)

model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def saludo():
    return render_template('indice.html')

@app.route('/predict', methods=['POST','GET'])
def predecir():
    int_features = [int(x) for x in request.form.values()]
    final =[np.array(int_features)]
    print(int_features)
    print(final)
    prediccion = model.predict_proba(final)
    salida = '{0:.{1}f}'.format(prediccion[0][1],2)
    print("Cantidad pred: ",salida)

    #{1}f a no olvidar significa un numero despues de la coma

    if salida > str (0.5):
        return render_template('indice.html', pred= 'El bosque se encuentra en peligro.\nLas Probabilidades de que ocurra un incendio es de {}'.format(salida), bhai="Hay algo por hacer ahora?")
    else:
        return render_template('indice.html', pred= 'El bosque se encuentra a salvo.\nLas Probabilidades de que ocurra un incendio es de {}'.format(salida), bhai="Todo se encuentra sano y salvo")

if __name__ == '__main__':
    app.run( debug=True)