import pandas as pd
import streamlit as st

df=pd.read_csv('book.csv')
st.title('Best Sellers')
st.write("This app shows the best sellers from 2009-2022")

books=df.shape[0]
Unique_Title=df['Name'].nunique()
Average_Rating=df['User Rating'].mean()
Average_Price=df['Price'].mean()

col1,col2,col3,col4=st.columns(4)

col1.metric('Total Books', books)
col2.metric("Unique Books",Unique_Title)
col3.metric('Average Rating',Average_Rating)
col4.metric('Average Price',Average_Price)