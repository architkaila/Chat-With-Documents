import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from html_templates import css, bot_template, user_template


def extract_text(pdf_file):
    """
    Function to extract the text from a PDF file

    Args:
        pdf_file (file): The PDF file to extract the text from

    Returns:
        text (str): The extracted text from the PDF file
    """

    # Initialize the raw text variable
    text = ""

    # Read the PDF file
    pdf_reader = PdfReader(pdf_file)

    # Extract the text from the PDF pages
    for page in pdf_reader.pages:
        text += page.extract_text()
    
    return text

def get_chunks(text):
    """
    Function to get the chunks of text from the raw text

    Args:
        text (str): The raw text from the PDF file

    Returns:
        chunks (list): The list of chunks of text
    """

    # Initialize the text splitter
    splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )

    # Get the chunks of text
    chunks = splitter.split_text(text)

    return chunks

def get_vectorstore(chunks):
    """
    Function to create avector store for the chunks of text to store the embeddings

    Args:
        chunks (list): The list of chunks of text

    Returns:
        vector_store (FAISS): The vector store for the chunks of text
    """

    # Initialize the embeddings model
    embeddings = OpenAIEmbeddings()

    # Create a vector store for the chunks of text
    vector_store = FAISS.from_texts(texts=chunks, embedding=embeddings)

    return vector_store

def get_conversation_chain(vector_store):
    """
    Function to create a conversation chain for the chat model

    Args:
        vector_store (FAISS): The vector store for the chunks of text
    
    Returns:
        conversation_chain (ConversationRetrievalChain): The conversation chain for the chat model
    """
    
    # Initialize the chat model
    llm = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0.1)

    # Initialize the chat memory
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    # Create a conversation chain
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vector_store.as_retriever(),
        memory=memory,
    )

    return conversation_chain

def generate_response(question):
    """
    Function to generate a response for the user query using the chat model

    Args:
        question (str): The user query

    Returns:
        response (str): The response from the chat model
    """

    # Get the response from the chat model
    response = st.session_state.conversations({'question': question})

    # Update the chat history
    st.session_state.chat_history = response['chat_history']

    # Add the response to the UI
    for i, message in enumerate(st.session_state.chat_history):
        # Check if the message is from the user or the chatbot
        if i % 2 == 0:
            st.write(user_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)


## Landing page UI
def run_UI():
    """
    The main UI function to display the UI for the webapp
    """

    # Load the environment variables
    load_dotenv()

    # Set the page tab title
    st.set_page_config(page_title="Chat with PDFs", page_icon="🤖", layout="wide")

    # Add the custom CSS
    st.write(css, unsafe_allow_html=True)

    # Initialize the session state variables
    if "conversations" not in st.session_state:
        st.session_state.conversations = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    # Set the page title
    st.header("Chat with Clinical Study Documents")

    # Input box for user query
    user_question = st.text_input("How can I help you?")

    # Generate the response if the user has entered a query
    if user_question:
        generate_response(user_question)

    # Sidebar menu
    with st.sidebar:
        st.subheader("Document Uploader")

        # Document uploader
        pdf_file = st.file_uploader("Upload a PDF you want to chat with", type="pdf", key="upload")

        # Process the document
        if st.button("Start Chatting ✨"):
            # Add a progress spinner
            with st.spinner("Processing"):
                # Convert the PDF to text
                raw_text = extract_text(pdf_file)
                
                # Get the chunks of text
                chunks = get_chunks(raw_text)
                
                # Create a vector store for the chunks of text
                vector_store = get_vectorstore(chunks)

                # Create a conversation chain
                st.session_state.conversations = get_conversation_chain(vector_store)

if __name__ == "__main__":
    run_UI()