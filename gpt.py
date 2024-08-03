from pandasai.llm import BambooLLM

import streamlit as st 
from pandasai.connectors import MySQLConnector
from pandasai import SmartDataframe


BAMBOO_API_KEY = "$2a$10$OFAyFRah.qPvQBwx.ENZM.1LH3YqrC3OntBtf3nd5A9jiK9eOLcJa"
my_connector = MySQLConnector(
    config={
        "host":"localhost",
        "port":3306,
        "database":"titanic",
        "username":"root",
        "password":"mysql",
        "table":"titanic",
    }
)

model = BambooLLM(api_key=BAMBOO_API_KEY)

## To connect directly with CSV

# df = SmartDataframe("titanic.csv", config={"llm": model})

# response = df.chat("How many people survived?")
# print(response)


df_connector = SmartDataframe(my_connector, config={"llm": model})

st.title("MySQL with LLM")

prompt = st.text_input("Enter your prompt:")

if st.button("Generate"):
    if prompt:
        with st.spinner("Generating response..."):
            st.write(df_connector.chat(prompt))

