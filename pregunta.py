"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")

    #
    # Inserte su código aquí
    #
    df["sexo"] =  df["sexo"].map(lambda x: x.lower())  #pasa a minusculas
    
    df["tipo_de_emprendimiento"] =  df["tipo_de_emprendimiento"].map(lambda y: y.lower())  #pasa a minusculas
    
    df["idea_negocio"] =  df["idea_negocio"].map(lambda y: y.lower()) #pasa a minusculas 
    df["idea_negocio"] = df["idea_negocio"].apply(lambda x : x.replace("-"," "))
    df["idea_negocio"] = df["idea_negocio"].apply(lambda x : x.replace("_"," "))
    #df["idea_negocio"] = df["idea_negocio"].apply(lambda x : x.replace("á","a"))
    #df["idea_negocio"] = df["idea_negocio"].apply(lambda x : x.replace("é","e"))
    #df["idea_negocio"] = df["idea_negocio"].apply(lambda x : x.replace("í","i"))
    #df["idea_negocio"] = df["idea_negocio"].apply(lambda x : x.replace("ó","o"))
    #df["idea_negocio"] = df["idea_negocio"].apply(lambda x : x.replace("ú","u"))
    df["idea_negocio"] = df["idea_negocio"].apply(lambda x : x.replace("."," "))
    
    df["barrio"] =  df["barrio"].map(lambda y: y.lower()) #pasa a minusculas 
    df["barrio"] = df["barrio"].apply(lambda x : x.replace("-"," "))
    df["barrio"] = df["barrio"].apply(lambda x : x.replace("_"," "))
    
    df["fecha_de_beneficio"] = pd.to_datetime(df["fecha_de_beneficio"] )
    
    df["monto_del_credito"] = df["monto_del_credito"].apply(lambda x : str(x).strip("$"))
    df["monto_del_credito"] = df["monto_del_credito"].apply(lambda x : x.replace(",",""))
    df["monto_del_credito"] = df["monto_del_credito"].apply(lambda x : x.replace("  ",""))
    df["monto_del_credito"] = df["monto_del_credito"].apply(lambda x : x.replace(" ",""))
    #tarjetas["monto_del_credito"] = tarjetas["monto_del_credito"].apply(lambda x : x.replace(".00",""))
    #tarjetas["monto_del_credito"] = tarjetas["monto_del_credito"].apply(lambda x : x.replace(".0",""))
    df["monto_del_credito"] = df["monto_del_credito"].astype(float)
    
    df["línea_credito"] = df["línea_credito"].apply(lambda x : x.replace("."," "))
    df["línea_credito"] = df["línea_credito"].apply(lambda x : x.replace("-"," "))
    df["línea_credito"] = df["línea_credito"].apply(lambda x : x.replace("_"," "))
    df["línea_credito"] = df["línea_credito"].apply(lambda x : x.replace("soli-diaria","soli diaria"))
    #tarjetas["línea_credito"] = tarjetas["línea_credito"].apply(lambda x : x.replace("soli diaria","solidaria"))
    df["línea_credito"] = df["línea_credito"].apply(lambda x : x.lower())

    #df.drop(['Unnamed: 0'], axis=1,inplace=True)
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)
    
    return df
