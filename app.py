import streamlit as st
from dotenv import load_dotenv

def main():
    load_dotenv()
    st.set_page_config(page_title="chat with multiple PDFs", page_icon=":books:")
    st.header("chat with multiple PDFs :books:")
    st.text_input("Ask question about your documents:")

    with st.sidebar:
        st.subheader("Your documnets")
        st.file_uploader("Upload your PDFs here and click on process")
        st.button("Process")

if __name__ == '__main__':
    main()