# DADOS NÃO ESTRUTURADOS

# CSV

import pandas as pd

dadosCSV = {
    
    "Nome": ["Ana", "Lucas", "Felipe", "Beatriz"],
    "Idade": [21, 18, 17, 20],
    "Cidade": ["Sao Paulo", "Fortaleza", "Sao Caetano do Sul", "Florianopolis"]
    
}

# CRIAR DATAFRAME (Linhas e Colunas)
df_csv = pd.DataFrame(dadosCSV)

# SALVAR EM CSV
df_csv.to_csv("DadosNão.csv", index= False)