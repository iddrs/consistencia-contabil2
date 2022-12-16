'''
Reporters salvam o resultado em algum lugar.
'''

import pandas as pd

class ScreenReporter:
    def __init__(self):
        pd.set_option('display.max_rows', None)
        self.df = pd.DataFrame(columns=['rule_name', 'left_value', 'right_value', 'difference'])

    def register(self, data):
        row = {'rule_name': [data['rule_name']],
              'left_value': ['{:,.2f}'.format(data['left']['total']).replace(',', '_').replace('.', ',').replace('_', '.')],
              'right_value': ['{:,.2f}'.format(data['right']['total']).replace(',', '_').replace('.', ',').replace('_', '.')],
              'difference': ['{:,.2f}'.format(data['difference']).replace(',', '_').replace('.', ',').replace('_', '.')]}
        df = pd.DataFrame.from_dict(row)
        self.df = pd.concat([self.df, df])

    def save(self):
        print(self.df)

class ExcelReporter:
    def __init__(self, file_output):
        self.file_output = file_output
        self.data = []

    def register(self, data):

        for item in data['left']['items']:
            row = {
                'rule_name': data['rule_name'],
                'left_table': item['table'],
                'left_field': item['field'],
                'left_filter': item['filter'],
                'left_invert': item['invert'],
                'left_value': item['value'],
                'left_total': None,
                'right_table': None,
                'right_field': None,
                'right_filter': None,
                'right_invert': None,
                'right_value': None,
                'right_total': None,
                'difference': None
            }
            self.data.append(row)
        for item in data['right']['items']:
            row = {
                'rule_name': data['rule_name'],
                'left_table': None,
                'left_field': None,
                'left_filter': None,
                'left_invert': None,
                'left_value': None,
                'left_total': None,
                'right_table': item['table'],
                'right_field': item['field'],
                'right_filter': item['filter'],
                'right_invert': item['invert'],
                'right_value': item['value'],
                'right_total': None,
                'difference': None
            }
            self.data.append(row)

        row = {
            'rule_name': data['rule_name'],
            'left_table': None,
            'left_field': None,
            'left_filter': None,
            'left_invert': None,
            'left_value': None,
            'left_total': data['left']['total'],
            'right_table': None,
            'right_field': None,
            'right_filter': None,
            'right_invert': None,
            'right_value': None,
            'right_total': data['right']['total'],
            'difference': data['difference']
        }
        self.data.append(row)

    def save(self):
        df = pd.DataFrame(self.data)
        df.to_excel(self.file_output, sheet_name='report', index_label='index')