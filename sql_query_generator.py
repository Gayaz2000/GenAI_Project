from dotenv import load_dotenv
import streamlit as st
import os
import sqlite3
import google.generativeai as genai

# Load environment variables
load_dotenv()

genai.configure(api_key = os.getenv('GOOGLE_API_KEY'))

# Function for Genai model
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt, question])
    return response.text

# Function to retrive query from DB
def read_sql_query(query, db):
    sanitized_query = query.strip("```").replace("sql", "").strip()
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sanitized_query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    return rows

# prompt
prompt = """
    You are an intelligent SQL generator. Your task is to understand natural language 
    descriptions and translate them into accurate SQL queries. Use the following guidelines:
    1. Parse the input carefully to identify the database structure, including table names, columns, 
    and relationships.
    2. Ensure that the query handles edge cases, such as null values, duplicates, or missing conditions, 
    where applicable.
    3. Provide the SQL query with proper syntax and formatting for readability.
    4. Avoid making assumptions about table names or columns unless explicitly stated in the input; 
    use placeholders where necessary.

"""

# Streamlit App
st.set_page_config(page_title = 'SQL query retriver')
st.header('Gemini pro to retrive SQL data')
question = st.text_input('Input: ', key = 'input')
submit =st.button('Ask the question')

### if submit is clicked
if submit:
    response = get_gemini_response(question, prompt)
    print(response)
    response = read_sql_query(response, 'student.db')
    st.subheader('The Response is : ')
    for row in response:
        print(row)
        st.header(row)
