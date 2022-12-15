'''
Pacote com as engines.

Engine é uma espécie de controller do processo de teste.
'''

'''
Engine básica para os testes.
'''

import sqlite3

class DefaultEngine:

    def __init__(self, repositories, reporters, rules):
        self.repositories = repositories
        self.reporters = reporters
        self.rules = rules

    def run_tests(self):
        # processa cada uma das regras
        for rule in self.rules:
            reporting = {}
            rule_spec = rule()
            rule_name = rule_spec[0]
            left_spec = rule_spec[1]
            right_spec = rule_spec[2]
            reporting['rule_name'] = rule_name
            reporting['left'] = {
                'items': [],
                'total': 0.0
            }
            reporting['right'] = {
                'items': [],
                'total': 0.0
            }
            # processa o valor esquerdo
            left_val = 0.0
            for subrule in left_spec:
                val = self.get_subrule_value(subrule)
                reporting['left']['items'].append({
                    'table': subrule[0],
                    'field': subrule[1],
                    'filter': subrule[2],
                    'invert': subrule[3],
                    'value': val
                })
                left_val += val
            reporting['left']['total'] = left_val
            # processa o valor direito
            right_val = 0.0
            for subrule in right_spec:
                val = self.get_subrule_value(subrule)
                reporting['right']['items'].append({
                    'table': subrule[0],
                    'field': subrule[1],
                    'filter': subrule[2],
                    'invert': subrule[3],
                    'value': val
                })
                right_val += val
            reporting['right']['total'] = right_val
            diff = round(left_val - right_val, 2)
            reporting['difference'] = diff
            self.report(reporting)

        self.save_report()


    def get_subrule_value(self, spec):
        table_name = spec[0]
        field = spec[1]
        filter = spec[2]
        invert = spec[3]
        if filter is None:
            sql_statement = f'SELECT SUM({field}) AS value FROM {table_name}'
        else:
            sql_statement = f'SELECT SUM({field}) AS value FROM {table_name} WHERE {filter}'
        connection = self.get_connection(table_name=table_name)
        val = self.sql_exec(connection=connection, sql_statement=sql_statement)
        val = val[0]
        if val == None:
            val = 0.0
        if invert:
            val = val *-1
        return round(val, 2)

    def sql_exec(self, connection, sql_statement):
        cur = connection.cursor()
        res = cur.execute(sql_statement)
        return res.fetchone()

    def get_connection(self, table_name):
        for repo in self.repositories:
            connection = repo.load(table_name)
            if connection is not None:
                return connection

    def report(self, data):
        for reporter in self.reporters:
            reporter.register(data)

    def save_report(self):
        for reporter in self.reporters:
            reporter.save()