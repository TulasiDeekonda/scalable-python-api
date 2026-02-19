import os
import json
from typing import Dict, Any
from openai import OpenAI
from fastapi import HTTPException

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Lazy client initialization
def get_client() -> OpenAI:
    if not OPENAI_API_KEY:
        raise HTTPException(
            status_code=503,
            detail="AI service is not configured. OPENAI_API_KEY is missing."
        )
    return OpenAI(api_key=OPENAI_API_KEY)


def analyze_text(text: str) -> Dict[str, Any]:
    """
    Analyze text using an LLM and return structured output.
    The function enforces a controlled JSON response format
    and fails gracefully if AI service is unavailable.
    """

    client = get_client()

    system_prompt = (
        "You are an assistant that analyzes text and returns structured JSON output only. "
        "Return a JSON object with the following keys: "
        "summary (string), keywords (list of strings), sentiment (positive, neutral, or negative)."
    )

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": text}
            ],
            temperature=0.2,
        )

        content = response.choices[0].message.content

        parsed = json.loads(content)

        required_keys = {"summary", "keywords", "sentiment"}
        if not required_keys.issubset(parsed.keys()):
            raise ValueError("Incomplete AI response structure")

        return parsed

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"AI service failed: {str(e)}"
        )
