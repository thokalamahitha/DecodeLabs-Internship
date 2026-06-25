import pandas as pd

df = pd.read_excel("C:\\Users\\Mahi\\OneDrive\\Desktop\\Dataset for Data Analytics.xlsx")
print(df.head())

print(df.info())
print(df.isnull().sum()) #NAN values are there only in the 'CouponCode' Column;

#filling the null values in 'CouponCode' column with 'NoCoupon' value;
df['CouponCode']=df['CouponCode'].fillna('N/A').str.upper()

#Checking Duplicates;

print(df['OrderID'].duplicated().sum()) # NO duplicated values;

#Formatting dates
df['Date']=pd.to_datetime(df['Date'],errors='coerce')
df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')

text_cols = ['OrderID','Product','ShippingAddress','PaymentMethod','OrderStatus','TrackingNumber','CouponCode','ReferralSource']

for col in text_cols:
    df[col] = df[col].astype(str).str.strip()

df['Product'] = df['Product'].str.title()
df['PaymentMethod'] = df['PaymentMethod'].str.title()
df['OrderStatus'] = df['OrderStatus'].str.title()
df['ReferralSource'] = df['ReferralSource'].str.title()

df['OrderID'] = df['OrderID'].str.upper()
df['CustomerID'] = df['CustomerID'].str.upper()
df['TrackingNumber'] = df['TrackingNumber'].str.upper()

df['UnitPrice']=pd.to_numeric(df['UnitPrice'],errors='coerce')
df['TotalPrice']=pd.to_numeric(df['TotalPrice'],errors='coerce')

df['UnitPrice']=df['UnitPrice'].round(2)
df['TotalPrice']=df['TotalPrice'].round(2)

print("\n After cleaning the data:\n")
print(df.head())
print(df.info())

df.to_excel(r"C:\\Users\\Mahi\\OneDrive\\Desktop\\Cleaned_dataset.xlsx",index=False)
