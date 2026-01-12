import streamlit as st
import functions



todos = functions.get_todos()
st.title('web app')

for todo in todos: 
    st.checkbox(todo)


st.text_input(label='', placeholder='new todo')

