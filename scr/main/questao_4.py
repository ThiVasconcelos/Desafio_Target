import pandas as pd

Faturamento_Mensal =  {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

Total_Faturamento_Mensal = sum(Faturamento_Mensal.values())
df_percentual_mensal = pd.DataFrame.from_dict(Faturamento_Mensal, orient='index', columns=['Faturamento Mensal'])
df_percentual_mensal.index.name = 'Estado'
df_percentual_mensal.reset_index(inplace=True)
df_percentual_mensal['Percentual Mensal'] = df_percentual_mensal['Faturamento Mensal'] / Total_Faturamento_Mensal * 100

print(df_percentual_mensal)

