'''
Pacote dos repositórios de dados.

Um repositório tem a função de fornecer para a engine as tabelas SQL necessárias para a execução de cada rule.
'''
import os.path
import sqlite3
import pandas as pd

class PadRepo:
    def __init__(self, path, entities):
        self.path = path
        self.entities = entities
        self.stage_path = r'./stage'

    def load(self, table_name):
        db_path = os.path.join(self.stage_path, f'{table_name}.db')
        if os.path.exists(db_path):
            pass
        else:
            self.generate_db(table_name=table_name)
        return sqlite3.connect(db_path)

    def generate_db(self, table_name):
        path = os.path.join(self.path, f'{table_name}.pickle')
        df = pd.read_pickle(path)
        df = self.entities_filter(df=df)
        db_path = os.path.join(self.stage_path, f'{table_name}.db')
        connection = sqlite3.connect(db_path)
        df.to_sql(table_name, connection)

    def entities_filter(self, df):
        # for entity in self.entities:
        #     filter = df['entidade'] == entity
        #     df = df[filter]
        df = df.loc[df['entidade'].isin(self.entities)]
        return df
