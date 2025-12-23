import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def translate_code(req):
    prompt = f"""
Translate this {req.source_lang} code to {req.target_lang}.
Preserve behavior exactly.

CODE:
{req.source_code}
"""
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
