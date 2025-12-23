from pydantic import BaseModel

class TranslateRequest(BaseModel):
    source_lang: str
    target_lang: str
    source_code: str

class ParityResult(BaseModel):
    parity: bool
    confidence: float
    source: dict
    target: dict
