import streamlit as st

# col1, col2, col3,col4 ,=st.columns(4,gap='small',vertical_alignment='center')

# with col1:
#     st.header("Col1")
#     st.write("Content")
# with col2:
#     st.header("Col2")
#     st.write("Content")
# with col3:
#     st.header("Col3")
#     st.write("Content")
# with col4:
#     st.header("Col4")
#     st.write("Content")

#SIDEBAR

# st.sidebar.header("Sidebar")

# st.sidebar.write("This is a sidebar")

# st.sidebar.selectbox("Choose one option",["Option 1", "Option 2" ,"Option 3" ])
# st.sidebar.radio("Go to",["Home","Data","Settings"])

#FORMS

with st.form("my_form" ,clear_on_submit=True):
    name=st.text_input('Name')
    age=st.slider("Age", min_value=0, max_value=100)
    email=st.text_input("Email")
    bio=st.text_area("Short bio")
    terms=st.checkbox('I agree to the terms and conditions')

    submit_button=st.form_submit_button(label='Submit')

if submit_button:
    st.write(f"Name:{name}")
    st.write(f"Age:{age}")
    st.write(f"Email:{email}")
    st.write(f"Desc:{bio}")
    
    if terms:
        st.write('You agrred to terms')
    else:
        st.write("You didnt agree to the terms")


with st.container():
    st.header("Best container")
    st.subheader("best Subheader")
    st.write("best write ever written")


tab1,tab2,tab3= st.tabs(["News",'Sport','Economy'])

with tab1():
    st.header('News')
    st.write("new News")

with tab2():
    st.header('Sport')
    st.write("News about Sport")

with tab3():
    st.header('Economy')
    st.write('Political and economical state of the world rn')