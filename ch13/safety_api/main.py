from fastapi import FastAPI, HTTPException
from .models import SafetyEnsemble, DummyLLM
from .schemas import PromptRequest, APIResponse, SafetyAnalysisResult
from .config import API_CONFIG
import uvicorn

app = FastAPI()
llm_generator = DummyLLM()

@app.post('/generate', response_model=APIResponse)
async def generate_safe(request: PromptRequest):
    try:
        safety = SafetyEnsemble()
        analysis_result = safety.analyze(request.prompt)
        
        if analysis_result['block']:
            reasons = self._get_block_reasons(analysis_result)
            return APIResponse(
                error="Content violation detected",
                reasons=reasons,
                details=analysis_result
            )
        else:
            return APIResponse(
                response=llm_generator.generate(request.prompt),
                details=analysis_result
            )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    def _get_block_reasons(self, analysis: dict) -> list[str]:
        reasons = []
        if analysis['toxicity_risk'] > MODEL_CONFIGS["toxicity"]["threshold"]:
            reasons.append("High toxicity")
        if analysis['fact_accuracy'] == MODEL_CONFIGS["factcheck"]["false_label"]:
            reasons.append("Factual inaccuracy")
        return reasons

if __name__ == "__main__":
    uvicorn.run(
        app,
        host=API_CONFIG["host"],
        port=API_CONFIG["port"],
        debug=API_CONFIG["debug"]
    )