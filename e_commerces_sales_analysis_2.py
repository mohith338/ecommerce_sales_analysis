import pandas as pd

df=pd.read_csv(r'C:\Users\User\Downloads\uncleaned_sales_dataset.csv')
df.head()
df.describe()
df.isnull().sum()
df.drop_duplicates(inplace=True)


print(df.duplicated().sum())

df.info()

df.columns=df.columns.str.strip().str.lower().str.replace(' ','_')
df.info()

df.drop_duplicates(subset='order_id', inplace=True)
print(df.duplicated().sum())

df['quantity']=df['quantity'].fillna(0)
df['unit_price_inr']=df['unit_price_inr'].fillna(0)

df['quantity']=pd.to_numeric(df['quantity'], errors='coerce').astype(int)
df['unit_price_inr']=pd.to_numeric(df['unit_price_inr'], errors='coerce').astype(int)
df.info()

df['total_amount_inr']=df['total_amount_inr'].replace('not available',0)
df['total_amount_inr']=df['total_amount_inr'].fillna(0)

df['total_amount_inr']=pd.to_numeric(df['total_amount_inr']).astype(int)
df.info()

df['discount_percent']=df['discount_percent'].replace('ten',0)
df['discount_percent']=df['discount_percent'].fillna(0)

df['discount_percent']=pd.to_numeric(df['discount_percent']).astype(int)
df.info()

df['order_id']=df['order_id'].fillna('unknown')
df['customer_id']=df['customer_id'].fillna('unknown')
df['order_date']=df['order_date'].fillna('unknown')
df['product']=df['product'].fillna('unknown')
df['city']=df['city'].fillna('unknown')
df['quantity']=df['quantity'].fillna(df['quantity'].mean())
df['unit_price_inr']=df['unit_price_inr'].fillna(df['unit_price_inr'].mean())
df['discount_percent']=df['discount_percent'].fillna(df['discount_percent'].mean())
df['total_amount_inr']=df['total_amount_inr'].fillna(df['total_amount_inr'].mean())
df['payment_method']=df['payment_method'].fillna('unknown')
df['order_status']=df['order_status'].fillna('unknown')

total_records=df.shape[0]
print('total_records', total_records)

quantity_analysis=df['quantity'].mean()
print('quantity_analysis', quantity_analysis)

unit_price_inr_analysis=df['unit_price_inr'].mean()
print('unit_price_inr_analysis', unit_price_inr_analysis)

discount_percent_analysis=df['discount_percent'].mean()
print('discount_percent_analysis', discount_percent_analysis)

total_amount_inr_analysis=df['total_amount_inr'].mean()
print('total_amount_inr_analysis', total_amount_inr_analysis)

result=df.columns.to_list()
print(result)

top_records=df.sort_values(by='total_amount_inr', ascending=False).head(10)
print(top_records[['order_id', 'customer_id', 'order_date', 'product', 'city', 'quantity', 'unit_price_inr', 'discount_percent','payment_method', 'order_status']
])

lower_records=df.sort_values(by='total_amount_inr', ascending=True).head(10)
print(lower_records[['order_id', 'customer_id', 'order_date', 'product', 'city', 'quantity', 'unit_price_inr', 'discount_percent','payment_method', 'order_status']
])

import matplotlib.pyplot as plt
df['total_amount_inr'].plot(kind='hist')
plt.title('analysis by total amount inr')
plt.xlabel('total_amount_inr')
plt.ylabel('quantity')
plt.show()

df['quantity'].plot(kind='hist')
plt.title('analysis by quantity with unit price int')
plt.xlabel('quantity')
plt.ylabel('unit_price_inr')
plt.show()

df['discount_percent'].plot(kind='hist')
plt.title('analysis by discount percent')
plt.xlabel('discount_percent')
plt.ylabel('total_amount_inr')
plt.show()

top_records.plot(kind='bar')
plt.title('top records analysis')
plt.show()

lower_records.plot(kind='bar')
plt.title('least records analysis')
plt.show()

df.to_csv('cleanned_ecommerces_sales_analysis_2.csv')
print('successfull')

import os
print(os.getcwd())

import sqlite3
conn = sqlite3.connect('cleanned_ecommerces_sales_analysis_2.db')
df.to_sql('cleanned_ecommerces_sales_analysis_2', conn, if_exists='replace')
conn.close()
print('done')




