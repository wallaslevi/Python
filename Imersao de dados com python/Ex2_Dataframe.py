import pandas as pd
import numpy as np

df_temperaturas = pd.DataFrame({
    "Dia": ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"], 
    "Temperatura": [30, np.nan, np.nan, 28, 27]
})

df_temperaturas["preenchido_ffill"] = df_temperaturas["Temperatura"].ffill()
df_temperaturas          #nova coluna com preenchimento automatico referente a coluna temperatura, ele pega o valor anterior da coluna temperatura

df_temperaturas["preenchido_bfill"] = df_temperaturas["Temperatura"].bfill()
df_temperaturas         #nova coluna com preenchimento automatico referente a coluna temperatura, ele pega o valor POSTERIOR da coluna temperatura

print(df_temperaturas)