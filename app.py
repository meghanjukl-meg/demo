import streamlit as st

st.title("Streamlit App")
st.header("This is header")

st.subheader("this is subheader")
st.text("Text")
st.write("TExt using write")

user_input = st.text_input("Write your text ")

st.write(user_input)
num_inpt = st.number_input("Enter your number")
st.write('Your number is ', num_inpt)

file_input = st.file_uploader('Upload your file')

st.button('Submit')

choice = st.radio('Choose an option', ['Option 1', 'Option 2'])

image = st.camera_input('Smile please')

st.write(":rainbow[this is rainbow text]")

st.write(":green[this is green text]")
