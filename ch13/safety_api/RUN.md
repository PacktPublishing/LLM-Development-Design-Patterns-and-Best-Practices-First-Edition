# Running the Safety API

## Starting the Server

1. **Navigate to project directory**:
   ```bash
   cd safety-api
   ```

2. **Activate virtual environment**:
   ```bash
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Run the API server**:
   ```bash
   python -m safety_api.main
   ```

   Expected output:
   ```
   INFO:     Started server process [12345]
   INFO:     Waiting for application startup.
   INFO:     Application startup complete.
   INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
   ```

## Testing the API

### Using cURL

1. **Test with safe content**:
   ```bash
   curl -X POST "http://localhost:8000/generate" \
   -H "Content-Type: application/json" \
   -d '{"prompt":"Explain quantum computing"}'
   ```

2. **Test with potentially toxic content**:
   ```bash
   curl -X POST "http://localhost:8000/generate" \
   -H "Content-Type: application/json" \
   -d '{"prompt":"I hate all people from this group"}'
   ```

### Using Python

```python
import requests

response = requests.post(
    "http://localhost:8000/generate",
    json={"prompt": "The Earth is flat"}
)
print(response.json())
```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/generate` | POST | Analyze and generate safe responses |

## Request Format
```json
{
  "prompt": "Your text to analyze"
}
```

## Response Format
Successful response:
```json
{
  "response": {
    "generated_text": "Safe response..."
  },
  "details": {
    "toxicity_risk": 0.12,
    "fact_accuracy": 2,
    "block": false
  }
}
```

Error response:
```json
{
  "error": "Content violation detected",
  "reasons": ["High toxicity"],
  "details": {
    "toxicity_risk": 0.95,
    "fact_accuracy": 1,
    "block": true
  }
}
```

## Stopping the Server
Press `CTRL+C` in the terminal where the server is running.