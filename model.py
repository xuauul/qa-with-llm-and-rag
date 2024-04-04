from langchain.llms import OpenAI
from langchain.chains import RetrievalQA

from utils import load_dotenv


class Model:
  def __init__(self, database):
    env_vars = load_dotenv()

    self.database = database

    llm = OpenAI(openai_api_key=env_vars.OPENAI_API_KEY, temperature=0)
    retriever = database.as_retriever()
    self.qa_model = RetrievalQA.from_chain_type(llm, chain_type="stuff", retriever=retriever)

  def run(self, query):
    # Retrieve similar document based on query
    similar_doc = self.database.similarity_search(query, K=1)[0]
    similar_doc_content = similar_doc.page_content

    # Run QA on retrieved document
    qa_output = self.qa_model.run(query)

    return similar_doc_content, qa_output