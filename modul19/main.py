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
    new_genre=st.selectbox("Genre" ,books["Genre"].unique())
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

st.sidebar.header('Filter options')
selected_author=st.sidebar.selectbox("Select author",['ALL']+list(books['Author'].unique()))
selected_year=st.sidebar.selectbox('Select year' ,['ALL']+list(books['Year'].unique()))
selected_genre=st.sidebar.selectbox('Select genre',["ALL"]+list(books['Genre'].unique()))
min_rating=st.sidebar.slider('Minimum rating',0.0,0.5,0.1)
max_price=st.sidebar.slider('Maximum price', 0, books['Price'].max(), books['Price'].max())

filtered_books=books.copy()

if selected_author !="All":
    filtered_books=filtered_books[filtered_books['Author']==selected_author]

if selected_year !='ALL':
    filtered_books=filtered_books[filtered_books["Year"]==int(selected_year)]

if selected_genre !='All':
    filtered_books=filtered_books[filtered_books["Genre"]==selected_genre]


filtered_books=filtered_books[
    (filtered_books['User Rating']>=min_rating) & (filtered_books["Price"]<=max_price)
]

st.subheader(" Summary Statistic")

total_books=filtered_books.shape[0]
unique_titles=filtered_books['Name'].nunique()
average_rating=filtered_books["User Rating"].mean()
average_price=filtered_books["Price"].mean()

col1, col2 ,col3 ,col4 =st.columns(4)
col1.metric("Total Books", total_books)
col2.metric("Unique Titles", unique_titles)
col3.metric("Average Rating", f"{average_rating:.2f}")
col4.metric("Average Price", f"{average_price:.2f}")


st.subheader("Dataset Preview")
st.write(filtered_books.head())


col1,col2=st.columns(2)

with col1:
    st.subheader("Top 10 book Titles")
    top_titles=filtered_books["Name"].value_counts().head(10)
    st.bar_chart(top_titles)

with col2:
    st.subheader("Top 10 Authors")
    top_authors=filtered_books['Author'].value_counts().head(10)
    st.bar_chart(top_authors)


st.subheader('Genre')
fig=px.pie(filtered_books,names="Genre", title="Most Liked Genres(2009-2025)", color="green",
color_disrete_sequence=px.colors.sequential.Plasma)
st.plotly_chart(fig)    