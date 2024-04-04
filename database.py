from pymongo import MongoClient
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain_community.vectorstores import MongoDBAtlasVectorSearch
from utils import load_dotenv


def initialize_vector_search_database():
    # Load environment variables
    env_vars = load_dotenv()

    # MongoDB settings
    database_name = "sample_mflix"
    collection_name = "embedded_movies"
    text_key = "fullplot"
    embedding_key = "plot_embedding"
    vector_search_index_name = "vector_index"

    # Connect to MongoDB
    mongo_client = MongoClient(env_vars.MONGO_URI)
    collection = mongo_client[database_name][collection_name]

    # Initialize OpenAI Embeddings
    openai_embeddings = OpenAIEmbeddings(openai_api_key=env_vars.OPENAI_API_KEY)

    # Initialize MongoDBAtlasVectorSearch
    database = MongoDBAtlasVectorSearch(
        collection,
        openai_embeddings,
        index_name=vector_search_index_name,
        embedding_key=embedding_key,
        text_key=text_key
    )
    return database