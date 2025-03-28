# DADOS ESTRUTURADOS

import pandas as pd

df_Excel = pd.read_excel("Dados Estruturados.xlsx", sheet_name=["aba1"])

# OPCIONAL CASO TENHA MAIS DE UMA ABA

df_aba1 = df_Excel["aba1"]

# -----------------------------------------

print(df_Excel)