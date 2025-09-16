import streamlit as st

user_input = st.text_input("Enter your name", "Type here...")
age = st.number_input("Enter your Age", )
weight = st.number_input("Enter your Weight", )
height = st.number_input("Enter your height", )
square=pow(height,2)
bmi= weight/square
    
if st.button("Calculate BMI"):
    st.write(f'Your BMI is {bmi}')
    if bmi<14:
        st.write('You are underweight')
    if 14<bmi<18:
        st.write("You are normal weight")
    if 18<=bmi<24:
        st.write('You are overweight')
    else:
        st.write('You are obese')

