# from googletrans import Translator
import pandas as pd
import numpy as np
# translator = Translator()



# data = pd.read_excel('semester 2\\class 4\\classwork\\grades.xlsx')
# a = translator.translate(data, dest='uk')
# print(a.text)



products = ['water', 'milk', 'melon', 'apple']
price = [15, 50, 200, np.nan]
data = pd.DataFrame(list(zip(products, price)), columns = ['products', 'price'])
# data.to_excel('semester 2\\class 4\\classwork\\groceries.xlsx', index=None)



with pd.ExcelWriter('semester 2\\class 4\\classwork\\groceries.xlsx') as writer:
    data.to_excel(writer, sheet_name='groceries1', index=None)
    data.to_excel(writer, sheet_name='groceries2', index = None)