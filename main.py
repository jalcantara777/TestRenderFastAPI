from fastapi import FastAPI, Query
from typing import List
import pandas as pd

app = FastAPI()

sucursales=pd.read_csv('Sucursales.csv', delimiter=';')
poss_vals = ["Cabildo", "Corrientes", "Almagro", "Caballito", "Flores"]
lst_suc_names=sucursales.Sucursal.to_list()

@app.get('/')
def message():
    return "Jehová Jireh"

@app.get('/sucursales_id')
def get_sucursal_address_from_integer(sucursal_id:int= Query(None, description="Ingrese un valor entero entre el rango 1-27")):
    linea1 = 'Sucursal : '+str.upper(sucursales.iloc[sucursal_id-1,1])
    linea2 = 'Dirección: '+sucursales.iloc[sucursal_id-1,2]
    valret = f"{linea1}    {linea2}"
    return valret

@app.get('/sucursales_name')
def get_sucursal_address_from_string(sucursal_name: str= Query(None, description=f"Ingrese desde las 3 primeras letras de los valores posibles de esta lista: {lst_suc_names}")):
    sucursal_id=sucursales[sucursales.Sucursal.str.lower().str.startswith(sucursal_name.lower())].ID.iloc[0]
    sucursal_nm=sucursales[sucursales.Sucursal.str.lower().str.startswith(sucursal_name.lower())].Sucursal.iloc[0]
    sucursal_ad=sucursales[sucursales.Sucursal.str.lower().str.startswith(sucursal_name.lower())].Direccion.iloc[0]
    linea1 = 'Sucursal : '+str.upper(sucursal_nm)+'    ID: '+str(sucursal_id)
    linea2 = 'Dirección: '+ sucursal_ad
    valret = f"{linea1}    {linea2}"
    #valret = linea1 +'    ID: '+str(sucursal_id)
    return valret
