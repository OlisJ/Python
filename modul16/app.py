import streamlit as st

# def main():
# st.title("Hello World")

# if __name__ == "__main__":
# main()

# if st.button("Click Me"):
#     st.write('Button clicked')

# if st.checkbox("Check me "):
#     st.write("Checkmate")

user_input = st.text_input("Enter your name", "Type here...")
st.write("Hello, ", user_input, "!")

age=st.number_input("Enter your age", min_value=0, max_value=100)
st.write(f"you are {age} years old")

if st.button("Success"):
    st.success('Operation was successful!')