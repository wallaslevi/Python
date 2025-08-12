import pandas as pd
import numpy as np

df_cidades= pd.DataFrame({
        'nome': ["Ana", "Bruno", "Carlos", "Daniele", "Val"],
    'cidade': ["São Paulo", np.nan, "Curitiba", np.nan, "Belém"]
})

df_cidades['cidade_preenchida'] = df_cidades['cidade'].fillna("Não informado") #nova coluna com preenchimento da informação "nao informado" 

df_limpo = df_cidades.dropna
print(df_cidades)