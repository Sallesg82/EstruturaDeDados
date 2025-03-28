# NÃO ESTRUTURADO
# JSON

import pandas as pd

dadosJSON = {
    
    "Nome": ["Ana", "Lucas", "Felipe", "Beatriz"],
    "Idade": [21, 18, 17, 20],
    "Cidade": ["Sao Paulo", "Fortaleza", "Sao Caetano do Sul", "Florianopolis"]
    
}

# CRIAR DATAFRAME
df_JSON = pd.DataFrame(dadosJSON)

# SALVAR EM JSON
df_JSON.to_json("dados semi.json", orient= "records", lines= False)