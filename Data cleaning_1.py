import pandas as pd
file='OSU Data.csv'
df = pd.read_csv(file, encoding='Big5')
print(df.columns)

df_1=df.drop(columns=['SKU','DESCRIPTION','MH SEGMENT','MH SUB-SEGMENT','MH CATEGORY','Customer Name','Entered by','Commission Salesperson','DOC_NUMBER','Start QOH','End QOH'])
print(df_1.columns)

df_1['Store'] = df_1['Store'].str.strip('0123456789-')
print(df_1.info())
df_1['Qty'] = df_1['Qty'].str.replace(',', '').astype(int)
print(df_1.info())


def convert_to_float(value):
    if isinstance(value, str):
        value = value.strip()
        if value.startswith('(') and value.endswith(')'):
            value = '-' + value[1:-1]
        value = value.replace('$', '').replace(',', '')
    return float(value)

df_1['Sales Price'] = df_1['Sales Price'].apply(convert_to_float)
df_1['Revenue'] = df_1['Revenue'].apply(convert_to_float)

city_info = {
    'Yakima': ['WA', '98902'],
    'Grandview': ['WA', '98930'],
    'Lynden': ['WA', '98264'],
    'Sunnyside': ['WA', '98944'],
    'Mattawa': ['WA', '99349'],
    'Pasco': ['WA', '99301'],
    'Buena': ['WA', '98953'],
    'Wenatchee': ['WA', '98801'],
    'McMinnville': ['OR', '97128'],
    'Milton Freewater': ['OR', '97862'],
    'Lafayette': ['OR', '97127'],
    'Medford': ['OR', '97501'],
    'Salem': ['OR', '97305'],
    'The Dalles': ['OR', '97058'],
    'Lodi': ['CA', '95240'],
    'Paso Robles': ['CA', '93446'],
    'Hanford CA': ['CA', '93230'],
    'New York': ['NY', '14551'],
    'Salem Clearwater': ['OR', '97305'],
    'Liquid Fertilizer Plant': ['OR', '97128'],
}

df_1['State'] = df_1['Store'].apply(lambda x: city_info[x][0] if x in city_info else 'Unknown')
df_1['Zip Code'] = df_1['Store'].apply(lambda x: city_info[x][1] if x in city_info else 'Unknown')


print(df_1.info())


df_1.to_csv('testing.csv', index=False, header=True)