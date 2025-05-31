# https://python.langchain.com/docs/how_to/#document-loaders
#pip install langchain
#pip install langchain-community
#pip install pypdf
import os
#from langchain.document_loaders import TextLoader, PyPDFLoader, UnstructuredWordDocumentLoader
from langchain_community.document_loaders import TextLoader, PyPDFLoader, UnstructuredWordDocumentLoader

file_path = "data/onboarding.txt"
loader = TextLoader(file_path)
docs = loader.load()



file_path = "data/spgi-annual-report-2023.pdf"
loader = PyPDFLoader(file_path)
docs2 = loader.load()


###
file_path = "data/data_roles.docx"

loader = UnstructuredWordDocumentLoader(file_path)
docs3 = loader.load()

print("Done")

