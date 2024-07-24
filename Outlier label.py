import pandas as pd
df=pd.read_csv('testing.csv')

df['Date'] = pd.to_datetime(df['Date'])
split_date = pd.Timestamp('2022-10-07')

df_before = df[df['Date'] < split_date]
df_after = df[df['Date'] >= split_date]

# df_before.to_csv('Check_1.csv', index=False)
# df_after.to_csv('Check_2.csv', index=False)
# print(df_before.info())
# print(df_after.info())

# df_before add new columns 'Median_Qty'
df_before['Median_Qty'] = df_before.groupby('Item ID')['Qty'].transform('median')
# 為 df_after add new columns 'Median_Qty'
df_after['Median_Qty'] = df_after.groupby('Item ID')['Qty'].transform('median')


# df_before add new columns 'Qty_Minus_Median'
df_before['Qty_Minus_Median'] = df_before['Qty'] - df_before['Median_Qty']
# df_after add new columns 'Qty_Minus_Median'
df_after['Qty_Minus_Median'] = df_after['Qty'] - df_after['Median_Qty']

# Calculate the maximum value of 'Qty_Minus_Median' in each 'Item ID'
max_qty_minus_median = df_after.groupby('Item ID')['Qty_Minus_Median'].max()

# Create a dictionary to record each 'Item ID' and its corresponding maximum value
item_max_dict = max_qty_minus_median.to_dict()

print(item_max_dict)

# Convert item_max_dict to Series for aligned indexing
max_qty_minus_median_series = pd.Series(item_max_dict)

# Create a new column 'Adjusted_Qty_Minus_Median' and adjust it based on the maximum value in the dictionary
df_before['Adjusted_Qty_Minus_Median'] = df_before.apply(lambda row: row['Qty_Minus_Median'] - max_qty_minus_median_series.get(row['Item ID'], 0), axis=1)

df_before.to_csv('Check_1.csv', index=False)

