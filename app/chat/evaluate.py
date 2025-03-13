import os

from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.core.evaluation import FaithfulnessEvaluator
from llama_index.llms.openai import OpenAI


def get_project_root() -> str:
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

llm = OpenAI(model="gpt-4o", temperature=0.0)

documents = SimpleDirectoryReader(get_project_root() + "/data").load_data()
index = VectorStoreIndex.from_documents(documents=documents, show_progress=True) 
evaluator = FaithfulnessEvaluator(llm=llm)

query_engine = index.as_query_engine(llm=llm)
response = query_engine.query(
    "内容描述的是王家豪的简历信息，包括姓名、教育背景、工作经历等， 注意是王家豪 如果其中名字或者我描述的环节不正确都要仔细检查"
)
eval_result = evaluator.evaluate_response(response=response)
print(str(eval_result.passing))