from unittest.mock import inplace

import pandas as pd

df=pd.read_csv("avgIQpercountry.csv")
print(df.info()) # we see the columns of this dataset
print(df.head()) # we see the first 5 rows

country_data=df['Country']
print(country_data)

subset=df[["Country","Average IQ"]]
filtered_DF=subset[subset['Average IQ']>100]
print(subset)
print(filtered_DF)



#Null_mask finding null rows
null_mask=df.isnull()
null_count=null_mask.sum()
print(null_count)


#Removing duplicates
df.drop_duplicates(keep="first",inplace=True)
