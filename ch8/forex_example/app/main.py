from fastapi import FastAPI, HTTPException
from app.chromadb_setup import get_chroma_collection
from app.services import (
    fetch_forex_data_alpha_vantage,
    generate_embedding,
    perform_inference_with_phi_model,
)

app = FastAPI()

# Initialize ChromaDB
collection = get_chroma_collection()

# --- Health Check Endpoint ---
@app.get("/health")
def health_check():
    """
    Health check to ensure the service is running.
    """
    return {"status": "ok"}

# --- Main Endpoint ---
@app.get("/process")
def process(
    from_currency: str = "USD",
    to_currency: str = "EUR",
    api_key: str = "YOUR_API_KEY",  # please create an api key from here https://alphavantage.co/support/#api-key
    query: str = "What is the current exchange rate for USD to EUR?",
):
    """
    Combines fetching forex data, storing it in ChromaDB,
    querying ChromaDB, and performing inference.
    """
    # Step 1: Fetch Forex Data
    forex_data = fetch_forex_data_alpha_vantage(from_currency, to_currency, api_key)
    if not forex_data:
        raise HTTPException(status_code=404, detail="Forex data not found.")

    # Step 2: Store Forex Data in ChromaDB
    for entry in forex_data:
        collection.add(
            documents=[f"Rate: {entry['rate']}"],
            metadatas=[{"currency_pair": entry["currency_pair"], "rate": entry["rate"]}],
            ids=[entry["currency_pair"]],
        )

    # Step 3: Query ChromaDB
    query_embedding = generate_embedding(query)
    db_results = collection.query(query_embeddings=[query_embedding], n_results=3)

    # Step 4: Perform Inference with vLLM Model
    inference_result = perform_inference_with_phi_model(query)

    return {
        "forex_data": forex_data,
        "db_results": db_results,
        "inference_result": inference_result,
    }
