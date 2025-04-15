import chromadb

def get_chroma_collection(collection_name="forex_data"):
    client = chromadb.Client()
    return client.create_collection(name=collection_name)
