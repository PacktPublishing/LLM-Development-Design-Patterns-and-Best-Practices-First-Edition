from pydantic import BaseModel

class PromptRequest(BaseModel):
    prompt: str

class SafetyAnalysisResult(BaseModel):
    toxicity_risk: float
    fact_accuracy: int
    block: bool

class APIResponse(BaseModel):
    response: dict | None = None
    error: str | None = None
    reasons: list[str] | None = None
    details: dict | None = None