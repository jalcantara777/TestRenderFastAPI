from fastapi import FastAPI
import pandas as pd

app = FastAPI()

df_suc=pd.read_csv('Sucursales.csv', delimiter=';')

@app.get('/')
def message():
    return "Jehová Jireh"

@app.get('/df_suc')
def get_sucursal_address(num_sucursal:int):
    valret = df_suc.iloc[num_sucursal,2]
    return 'La dirección de la sucursal de '+str.upper(df_suc.iloc[num_sucursal,1])+ ' es: '+valret
