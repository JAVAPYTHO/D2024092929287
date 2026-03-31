import chardet
import pandas as pd
from collections import Counter
import os

script_dir = '../Processed appendices/'


file1_path = os.path.join(script_dir, 'Science, education, and culture data_3.csv')
file2_path = os.path.join(script_dir, 'Science, education, and culture data_4.csv')
output_path = os.path.join(script_dir, '../The generated images and files/Comparison chart of the number of services/Science, education, and culture data.xlsx')

with open(file1_path, 'rb') as f:
    result = chardet.detect(f.read())
with open(file2_path, 'rb') as f:
    result2 = chardet.detect(f.read())

encoding = result['encoding']
encoding2 = result2['encoding']

df1 = pd.read_csv(file1_path, encoding=encoding)
df2 = pd.read_csv(file2_path, encoding=encoding2)

column1 = df1.iloc[:, 1].astype(str).str.replace(r'\|.*$', '', regex=True)
column2 = df2.iloc[:, 1].astype(str).str.replace(r'\|.*$', '', regex=True)

counter1 = Counter(column1)
counter2 = Counter(column2)
all_elements = set(list(counter1.keys()) + list(counter2.keys()))
all_elements_count = {element: (counter1.get(element, 0), counter2.get(element, 0)) for element in all_elements}

result_df = pd.DataFrame.from_dict(all_elements_count, orient='index', columns=['City 1', 'City 2'])

total_sum = result_df.sum(numeric_only=True)
result_df.loc['Total'] = total_sum

result_df.to_excel(output_path, index_label='Element')