import pandas as pd

# Leer archivo XLSX y convertir a CSV
df = pd.read_excel('311_ServiceRequest_2010-Present_DataDictionary_Updated_2023.xlsx')
df.to_csv('nyc_311.csv', index=False)

