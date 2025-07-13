from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
from .config import MODEL_CONFIGS

class SafetyEnsemble:
    def __init__(self):
        try:
            # Initialize toxicity model
            self.toxicity_tokenizer = AutoTokenizer.from_pretrained(
                MODEL_CONFIGS["toxicity"]["model_name"])
            self.toxicity_model = AutoModelForSequenceClassification.from_pretrained(
                MODEL_CONFIGS["toxicity"]["model_name"])
            
            # Initialize fact-checking model
            self.factcheck_tokenizer = AutoTokenizer.from_pretrained(
                MODEL_CONFIGS["factcheck"]["model_name"])
            self.factcheck_model = AutoModelForSequenceClassification.from_pretrained(
                MODEL_CONFIGS["factcheck"]["model_name"])
            
        except Exception as e:
            raise RuntimeError(f"Model loading failed: {str(e)}")

    def analyze(self, text: str) -> dict:
        try:
            # Toxicity analysis
            tox_inputs = self.toxicity_tokenizer(
                text, return_tensors="pt", truncation=True, max_length=512)
            tox_score = self._get_toxicity_score(tox_inputs)

            # Fact-checking analysis
            fc_inputs = self.factcheck_tokenizer(
                text, return_tensors="pt", truncation=True, max_length=512)
            veracity = self._get_veracity_score(fc_inputs)

            return {
                "toxicity_risk": tox_score,
                "fact_accuracy": veracity,
                "block": (tox_score > MODEL_CONFIGS["toxicity"]["threshold"] or 
                         veracity == MODEL_CONFIGS["factcheck"]["false_label"])
            }
        except Exception as e:
            raise RuntimeError(f"Analysis failed: {str(e)}")

    def _get_toxicity_score(self, inputs):
        self.toxicity_model.eval()
        with torch.no_grad():
            outputs = self.toxicity_model(**inputs)
        return torch.sigmoid(outputs.logits).item()

    def _get_veracity_score(self, inputs):
        self.factcheck_model.eval()
        with torch.no_grad():
            outputs = self.factcheck_model(**inputs)
        return torch.argmax(outputs.logits).item()


class DummyLLM:
    def generate(self, prompt: str) -> dict:
        return {"generated_text": f"This is a safe response to: '{prompt}'."}