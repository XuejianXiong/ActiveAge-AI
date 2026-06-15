import os
from dotenv import load_dotenv

from langchain.tools import tool
from langchain_openai import OpenAIEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


load_dotenv('.secrets')
if not os.environ.get("OPENAI_API_KEY"):
    raise ValueError("Missing OPENAI_API_KEY environment variable")


#######################################
# Setup the embeddings to use the Gateway 
#######################################
'''
# This is for ChatGPT model
embeddings_model = OpenAIEmbeddings(
    openai_api_base='https://k7uffyg03f.execute-api.us-east-1.amazonaws.com/prod/openai/v1',
    openai_api_key="any value",
    default_headers={"x-api-key": os.getenv('API_GATEWAY_KEY')},
    model="text-embedding-3-small"
)
'''

# This is for local Gemma model from LM Studio
embeddings_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


#######################################
# Point to the vectorDB folder
#######################################
vector_db = Chroma(
    #persist_directory="data/chroma_db", 
    persist_directory="data/chroma_db_df", 
    embedding_function=embeddings_model
)


#######################################
# Create the Tool
#######################################
@tool
def get_mental_activity(query: str):
    """
    Resolves questions about mental health, mental exercises, or brain exercises 
    using a semantic search across a curated dataset.
    """
    docs = vector_db.similarity_search(query, k=3)
    
    if not docs:
        return "I couldn't find a matching mental exercise."
        
    return f"Exercise: {docs[0].metadata['Exercise Name']}\nInstructions: {docs[0].page_content}"