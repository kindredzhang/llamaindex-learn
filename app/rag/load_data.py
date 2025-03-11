from llama_index.core import SimpleDirectoryReader
from llama_index.core import VectorStoreIndex
from llama_index.core import Document
from llama_index.core import SimpleDirectoryReader
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.schema import TextNode
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core.settings import Settings
from llama_index.llms.openai import OpenAI
import os

def get_project_root() -> str:
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

async def main():
    # manual LLM
    llm = OpenAI(model = "gpt-4o")
    # manual text splitter
    text_splitter = SentenceSplitter(chunk_size=100, chunk_overlap=20)
    # settings~
    Settings.llm = llm
    Settings.transformations = [text_splitter]

    # support parsing including .md, .pdf, .jpg, .png, .docx, as well as audio and video types.
    # browse LlamaHub directly to see the hundreds of connectors available

    # ---- Document Creation ----

    # use api create documents
    documents = SimpleDirectoryReader(get_project_root() + "/data").load_data()

    # manual create documents
    # document1 = Document(text="Hello world!")
    # add metadata to documents, mainly used for search record data's source
    # document2 = Document(text="Hello llamaindex!", metadata={"source": "manual", "filename": "manual.txt"})
    # documents = [document1, document2]

    # ---- Index Creation ----

    # use api auto splitter chunk create index 
    # show_progress is a optional parameter, default is False
    index = VectorStoreIndex.from_documents(documents=documents, show_progress=True) 

    # manual create index    
    # index = VectorStoreIndex.from_documents(documents=documents, transformations=[text_splitter])

    # ---- Optional(create & passing nodes) ----
    # node1 = TextNode(text="i am kindred zhang, a Ai developer engineer")
    # index.insert_nodes([node1])
    # node2 = TextNode(text="you are a assistant of llama index")
    # manual_index = VectorStoreIndex([node2])
    
    # At this point, the vector preparation work for rag is complete. The basic process is as follows:
    # 1. get source files
    # 2. create document
    # 3. create nodes
    # 4. create index
    print("----index----")
    print(index)
    # print("----manual_index----")
    # print(manual_index)
    
    # ---- Query ----
    
    query_engine = index.as_query_engine()

    # query 
    # this step is the final step of rag (use user's query to get relevant info, location source files)
    response = query_engine.query("Test Engineer")
    print(response)
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
