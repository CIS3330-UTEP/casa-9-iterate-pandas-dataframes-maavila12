import pandas as pd
filename = './big-mac-full-index.csv'
data = {'Item': ['Apple', 'Banana', 'Orange'],'Quantity': [10, 20, 30],'Price': [0.5, 0.3, 0.7]}
df = pd.DataFrame(data)

# Iterating over rows
for index, row in df.iterrows():
    total_sales = row['Quantity'] * row['Price']
    print(f"{row['Item']} Total Sales: ${total_sales}")


    import pandas as pd

data = {'Item': ['Apple', 'Banana', 'Orange'],'Quantity': [10, 20, 30],'Price': [0.5, 0.3, 0.7]}
df = pd.DataFrame(data)
# Iterating using itertuples()
for row in df.itertuples():
    total_sales = row.Quantity * row.Price
    print(f"{row.Item} Total Sales: ${total_sales}")
