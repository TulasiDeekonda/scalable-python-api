import os
from typing import Dict, Any
from openai import OpenAI
from fastapi import HTTPException

# Environment-based API key (never hardcode secrets)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY environment variable not set")

client = OpenAI(api_key=OPENAI_API_KEY)


def analyze_text(text: str) -> Dict[str, Any]:
    """
    Analyze text using an LLM and return structured output.
    The function enforces a controlled JSON response format.
    """

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

        # We expect structured JSON from the model
        import json
        parsed = json.loads(content)

        # Basic validation
        if not all(k in parsed for k in ["summary", "keywords", "sentiment"]):
            raise ValueError("Incomplete AI response structure")

        return parsed

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"AI service failed: {str(e)}"
        )
