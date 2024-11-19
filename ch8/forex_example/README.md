# Forex Data & Intelligent Query System

## Problem Statement
The goal of this project is to create a system capable of fetching real-time foreign exchange (forex) rates, analyzing them, and answering user queries using natural language processing (NLP). Key challenges include:

- Fetching accurate and up-to-date forex data from APIs.
- Efficiently storing forex data for rapid querying and analysis.
- Leveraging intelligent language models for insightful, query-based responses.

## Solution
The solution integrates **FastAPI** for building web services, **ChromaDB** for storing forex data, and **LLMs model** with Hugging Face's pre-trained models for inference. This system fetches forex data, stores it, and provides NLP-powered insights based on user queries.

- **FastAPI** is used for handling HTTP requests.
- **ChromaDB** efficiently stores forex data and enables quick retrieval.


## Installation

### Requirements
To run this project, ensure you have the following installed:

- Python 3.x
- FastAPI
- ChromaDB
- Sentence Transformers
- Requests (for fetching forex data)

### Installation Steps

1. **Clone the repository:**

2. **Install dependencies:**
You can install the required packages using `pip` or `pipx` (if you're using pipx to isolate environments).

With `pip`:
```bash
 pip install -r requirements.txt
```

3. **Run the application:**
Start the FastAPI server:

```bash
uvicorn main --reload
```

## Usage

### Health Check Endpoint
- **URL**: `/health`
- **Method**: `GET`
- **Description**: Use this endpoint to check if the API is running.
- **Response**: A simple status message indicating the system is up and running.

### Process Endpoint
- **URL**: `/process`
- **Method**: `GET`
- **Parameters**:
- `from_currency`: (e.g., "USD")
- `to_currency`: (e.g., "EUR")
- `api_key`: Your Alpha Vantage API key.
- `query`: The natural language query (e.g., "What is the current exchange rate for USD to EUR?").
- **Description**: This endpoint fetches the latest forex data, stores it in ChromaDB, and uses the Hugging Face model for intelligent inference based on the user's query.
- **Response**: A JSON object containing the fetched forex data, database query results, and inference results.

## Testing with Postman

### Health Endpoint
1. Open Postman and create a new `GET` request.
2. Use the URL `http://localhost:8000/health`.
3. Click **Send** to check the health of the API.

### Process Endpoint
1. Open Postman and create a new `GET` request.
2. Use the URL `http://localhost:8000/process`.
3. Under **Params**, add the following keys:
- `from_currency`: e.g., `USD`
- `to_currency`: e.g., `EUR`
- `api_key`: Your API key.
- `query`: e.g., `"What is the current exchange rate for USD to EUR?"`
4. Click **Send** to get the forex data and intelligent response.

## License
MIT License. See LICENSE file for details.

