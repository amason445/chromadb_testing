import chromadb.utils.embedding_functions as embedding_functions

openai_ef = embedding_functions.OpenAIEmbeddingFunction(
    api_key= "",
    model_name="text-embedding-3-small"
)
