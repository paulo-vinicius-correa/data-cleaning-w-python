# data-cleaning-w-python
Limpando dados de arquivos CSV utilizando Python. Técnicas e práticas recomendadas para tratar dados incompletos, inconsistentes ou fora de padrão.

## Objetivo: 
Criar um script simples em Python para importar dados de arquivos CSV ou Excel, limpar e realizar algumas transformações básicas (como remover valores nulos, corrigir tipos de dados, etc.) e salvar os dados tratados em outro arquivo ou banco de dados.
### Habilidades:
Manipulação de dados com pandas.
Leitura e escrita de arquivos CSV/Excel.
Limpeza básica de dados (remoção de duplicados, valores nulos, formatação).


#### Codigo para baixar os dados: 

``` python
import kagglehub

path = kagglehub.dataset_download("mohammedarfathr/customer-transactions-dataset")

print("Path to dataset files:", path)
```