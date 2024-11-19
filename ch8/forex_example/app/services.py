import logging
import requests
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForCausalLM

# Fetch Forex Data
def fetch_forex_data_alpha_vantage(from_currency, to_currency, api_key):
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "FX_DAILY",
        "from_symbol": from_currency,
        "to_symbol": to_currency,
        "apikey": api_key,
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        if "Time Series FX (Daily)" in data:
            latest_data = next(iter(data["Time Series FX (Daily)"].values()))
            return [{
                "currency_pair": f"{from_currency}/{to_currency}",
                "rate": latest_data["4. close"],
            }]
        else:
            logging.error("Forex data not found.")
            return []
    except requests.exceptions.RequestException as e:
        logging.error(f"API error: {e}")
        return []

# Generate Embedding for Query
def generate_embedding(query):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    return model.encode(query).tolist()

# Perform Inference
def perform_inference_with_phi_model(query):
    model_name = "microsoft/phi-1_5"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)

    inputs = tokenizer(query, return_tensors="pt")
    outputs = model.generate(inputs["input_ids"], max_length=100, num_return_sequences=1, do_sample=True)
    
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
