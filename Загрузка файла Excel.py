import pandas as pd

url = 'https://tinyurl.com/simulated-excel'

dataframe = pd.read_excel(url, sheet_name=0, header=1)
print(dataframe.head(2))

# sheet_name указывает, какой лист в файле Excel мы хотим загрузить

