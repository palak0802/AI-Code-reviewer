import streamlit as st
from openai import openai

st.title('GenAI App - AN AI Code Reviewer')
st.header('Code Reviewer....')

API_KEY = "sk-proj-rZZcny1cuz4E61OI8wBdT3BlbkFJj8EdNMMNpmlCfC2bVeFh"

client = openai(api_key=API_KEY)

query = st.text_area('Enter Your Query : ')
if st.button('Generate'):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": query}
        ]
    )
    st.write(response.choices[0].message.content)
