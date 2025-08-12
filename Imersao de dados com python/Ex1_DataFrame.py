import pandas as pd
import numpy as np

df_salarios =pd.DataFrame({
    'nome':["Pai","Mãe","Filho","Avó","Tio"],
    'salario':[4000,np.nan,5000,np.nan,100000]
})

df_salarios['salario_media'] = df_salarios['salario'].fillna(df_salarios['salario'].mean().round(2))    #vai incluir nova coluna chamada salario_media e preencher a coluna salario na parte que os valores estao nulos colocando a media com 2 digitos

df_salarios['salario_mediana'] = df_salarios['salario'].fillna(df_salarios['salario'].median()) #Em vez de calcular pela media vai calcular pela mediana sem arredondar 2 casas decimais

print(df_salarios)