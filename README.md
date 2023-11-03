# Chat-With-Documents 💬
> #### _OpenAI | GPT-3.5 | Langchain | StreamLit_ 
&nbsp;

## Project Description ⭐  
Imagine having a conversation with your own data, asking questions, and getting responses as if the document itself could understand and talk back to you. [`Chat-With-Documents`](https://chatwithdocuments.streamlit.app) helps build a seamless and intuitive way to extract knowledge from your documents.

This project is an implementation of a `Retrieval Augmented Generation`(RAG) System. It leverages the power of Python, LangChain, and the GPT-3.5 Turbo model API from OpenAI to create an interactive chat experience with any PDF or document you have. 

## How It Works

1. **Upload Your Documents**: Users can easily upload any PDF(s) or document directly into the Streamlit app. The app supports multiple file formats, including PDF, DOCX, and TXT.
2. **Intelligent Parsing and Chunking**: Once uploaded, the app parses and extracts the text from the document(s).
3. **Embedding and Indexing**: The chunked text is then embedded using state-of-the-art embedding models and stored in a `FAISS` (Facebook AI Similarity Search) database. This process optimizes the retrieval of information and ensures that your queries are answered with precision.
4. **Conversational Interface**: Users can then navigate to the chat section of the app, where they can ask questions and engage in dialogue. The embedded documents serve as context, providing the GPT-3.5 powered chatbot with the information needed to generate accurate and contextually relevant responses.
5. **Retrieval-Augmented Generation (RAG)**: At the heart of this peoject is a RAG system that combines the benefits of a powerful retrieval system with the generative capabilities of GPT models. This allows for a conversational experience that is not just reactive but truly interactive, providing users with a novel way to explore and understand their data.

&nbsp;
## Running the Application 🧨  
Following are the steps to run the StreamLit Application: 


**1. Create a new conda environment and activate it:** 
```
conda create --name chat-with-documents python=3.8.17
conda activate chat-with-documents
```
**2. Install python package requirements:** 
```
pip install -r requirements.txt 
```
**4. Add OpenAI API Key**
```
Rename the env.example file to .env and add your OpenAI API key
```
**5. Run the application**
```
streamlit run app.py
```

&nbsp;  
## Project Structure 🧬  
The project data and codes are arranged in the following manner:

```
├── assets                              <- directory for repository image assets
├── .gitignore                          <- git ignore file
├── app.py                              <- Streamlit app file
├── env.example                         <- Environment variables file for API keys
├── html_chatbot_template.py            <- HTML/CSS template for chatbot
├── LICENSE                             <- license file
├── README.md                           <- description of project and how to set up and run it
├── requirements.txt                    <- requirements file to document dependencies
```  

