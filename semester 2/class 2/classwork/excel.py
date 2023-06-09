import pandas as pd
# data = pd.read_excel('semester 2\\class 2\\grades.xlsx', sheet_name=['student 2', 'student 1'])
data = pd.read_excel('semester 2\\class 2\\grades.xlsx', usecols=['subject', 'grade'])
print(data)