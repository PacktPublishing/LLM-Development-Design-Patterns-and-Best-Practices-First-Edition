# Model configurations
MODEL_CONFIGS = {
    "toxicity": {
        "model_name": "facebook/roberta-hate-speech-dynabench-r4-target",
        "threshold": 0.9
    },
    "factcheck": {
        "model_name": "digitalepidemiologylab/covid-twitter-bert-v2-finetuned-factcheck",
        "false_label": 0
    }
}

# API settings
API_CONFIG = {
    "host": "0.0.0.0",
    "port": 8000,
    "debug": True
}