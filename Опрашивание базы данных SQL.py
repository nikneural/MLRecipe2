import pandas as pd
from sqlalchemy import create_engine


database_connection = create_engine('sqlite:///sample.db')

dataframe = pd.read_sql_query("SELECT * FROM data", database_connection)

print(dataframe.head(2))

# применяем функцию create_engine для установления подключения к ядру быза дынных SQL
