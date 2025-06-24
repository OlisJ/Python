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



#finding the average of a continent

avg_iq_per_country=df.groupby('Continent')["Average IQ"].mean()

avg_iq_per_country=avg_iq_per_country.sort_values(ascending=True)
print(avg_iq_per_country)

#calculate nobel prizes by country , and show countries  only with more than 1 nobel
#you have to use  Groupby, Sum and sort values

nobel_country=df.groupby("Country")['Nobel Prices'].sum()
sorted_nobel_country=nobel_country.sort_values(ascending=False)
sorted_nobel_country=sorted_nobel_country[sorted_nobel_country!=0]
print(sorted_nobel_country)