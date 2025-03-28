# Dados Estruturados - Criação
# Exel

#---------------------------------
# NECESSÁRIO INSTALAR

#pip install openpyxl
#pip install pandas

#---------------------------------

import pandas as pd
# ESTRUTURA DE DICIONÁRIO   
dadosPlanilha = {
    
    "Nome": ["Ana", "Lucas", "Felipe", "Beatriz"],
    "Idade": [21, 18, 17, 20],
    "Cidade": ["Sao Paulo", "Fortaleza", "Sao Caetano do Sul", "Florianopolis"]
    
}

df_Planilha = pd.DataFrame(dadosPlanilha)

# CRIAR UM DATAFRAME (LINHA E COLUNAS)
df_Planilha = pd.DataFrame(dadosPlanilha)


# SALVAR NO EXEL
with pd.ExcelWriter("Dados Estruturados.xlsx") as writer:
    df_Planilha.to_excel(writer, sheet_name= "aba1", index= False)