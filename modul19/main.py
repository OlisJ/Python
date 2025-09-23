import pandas as pd
import streamlit as st
import plotly.express as px

books=pd.read_csv('book.csv')

st.title("Bestseller Books")
st.write('Best selling book analysis')

st.sidebar.header('Add new book')
  
with st.sidebar.form("book_form"):
    new_user=st.text_input("Book name")
    new_author=st.text_input('Authors name')
    new_user_rating=st.slider('User Rating', 0.5 , 5.0 ,0.0,0.1)
    new_reviews=st.number_input( "Reviews" ,min_value=0 ,step=1, max_value=5)
    new_genre=st.text_input("Genre" ,books["Genre"].nunique())
    new_price=st.number_input("Price...",min_value=1,step=1)
    new_year=st.number_input("Year of Publishing", min_value=2009,max_value=2025)
    submit_button=st.form_submit_button('Add book')

    if submit_button:
        new_data={
            "Name":new_user,
            "Author":new_author,
            "Rating":new_user_rating,
            "Review":new_reviews,
            "Genre":new_genre,
            "Price":new_price,
            'Year':new_year
        }

        books=pd.concat([pd.DataFrame(new_data, index=[0]),books],ignore_index=True)
        books.to_csv('book.csv', index=False)
        st.sidebar.success("New book has been added")