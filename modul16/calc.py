import streamlit as st

num1=st.number_input("Enter a value", min_value=0, max_value=100)
num2=st.number_input("Enter a second value", min_value=0, max_value=100)
if st.button("Multiply"):
    st.write(f"The result is {num1*num2}")
if st.button("Divide"):
    st.write(f"The result is {num1/num2}")

if st.button("Add"):
    st.write(f"The result is {num1+num2}")

if st.button("Subtract"):
    st.write(f"The result is {num1-num2}")

