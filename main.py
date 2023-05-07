from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
import streamlit as st

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def csv_llm():
    st.header('Welcome to CSV QnA')
    openai_key =st.text_input('Please enter your OpenAI key here', type="password")
    csv_file = st.file_uploader(label='Upload your CSV file',type='csv')
    if csv_file is not None:
        agent = create_csv_agent(OpenAI(temperature=0,openai_api_key= openai_key), path=csv_file)
        query = st.text_input('Enter your Natural language query below:')
        submit = st.button('Submit')
        st.write('Press submit to have your query answered')
        if submit:
            st.write("Answer: " + agent.run(query))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    csv_llm()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
