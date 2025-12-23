from fastapi import FastAPI
from app.models import TranslateRequest, ParityResult
from app.translate import translate_code
from app.run import run_code
from app.verify import verify_outputs

app = FastAPI(title="Parity API")

@app.post("/verify", response_model=ParityResult)
def verify(req: TranslateRequest):
    translated = translate_code(req)
    src_out = run_code(req.source_code, req.source_lang)
    tgt_out = run_code(translated, req.target_lang)
    return verify_outputs(src_out, tgt_out)
