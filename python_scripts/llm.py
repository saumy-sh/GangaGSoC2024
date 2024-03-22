import os
import sys

from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores.faiss import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain_openai import OpenAI
from langchain_community.chat_models import ChatOpenAI
###############################include your API key here###########################################
os.environ["OPENAI_API_KEY"] = "GIVE YOUR OpenAI API KEY HERE"
#this key can be generated using openai platform ad generating keys from API keys section
query = sys.argv[1]
print(query)

reader = open("data.txt","r")
data = reader.read()

text_splitter = CharacterTextSplitter(chunk_size = 1000, chunk_overlap = 100)
texts = text_splitter.split_text(data)

embeddings = OpenAIEmbeddings()
docsearch = FAISS.from_texts(texts,embeddings)

chain = load_qa_chain(OpenAI(),chain_type = "stuff")
docs = docsearch.similarity_search(query)
output = chain.invoke({"input_documents":docs,"question":query,"llm": ChatOpenAI})
print(output["output_text"])