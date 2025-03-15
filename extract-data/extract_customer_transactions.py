import os
import pandas as pd

# definindo variaveis para não depender de caminho absolutos
extract_data = os.getcwd()
folder_data = os.path.join(os.path.dirname(extract_data), 'data')
data_unclean = os.path.join(folder_data, 'unclean_customer_data.csv')

# lendo o arquivo
unclean = pd.read_csv(data_unclean)

def clean_data (unclean):
    # copiando o data frame
    unclean_copy = unclean.copy()

    # preenchendo os valores NaN com 0
    unclean_copy = unclean_copy.fillna(0)

    # alterando o tipo de dados para float
    unclean_copy ['Transaction_Amount'] = unclean_copy['Transaction_Amount'].astype(float)

    # alterando o tipo de dados para string
    unclean_copy ['Age'] = unclean_copy ['Age'].astype(str)

    # alterando o tipo de dados para string
    unclean_copy ['Customer_ID'] = unclean_copy ['Customer_ID'].astype(str)

    # removendo espaços no ID do Cliente
    unclean_copy ['Customer_ID'] = unclean_copy ['Customer_ID'].str.strip()

    return unclean_copy

cleaned_data = clean_data(unclean)
print(cleaned_data.head(2))