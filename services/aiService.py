import os
import httpx
from fastapi import HTTPException
from models.requestModel import RequestModel
from models.responseModel import ResponseModel
from utils.logger import logger

async def handle_ai_request(request: RequestModel) -> ResponseModel:
    """
    Handles requests to the OpenAI API and returns a formatted response.
    
    Args:
        request (RequestModel): The request containing prompt and max_tokens.
        
    Returns:
        ResponseModel: The formatted response containing the AI-generated output.
    """
    try:
        # Validate the prompt is not empty
        if not request.prompt.strip():
            raise ValueError("Prompt cannot be empty")
        
        async with httpx.AsyncClient() as client:
            # Make a request to the OpenAI API
            response = await client.post(
                "https://api.openai.com/v1/engines/davinci/completions",
                headers={
                    "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}",
                    "Content-Type": "application/json"
                },
                json={
                    "prompt": request.prompt,
                    "max_tokens": request.max_tokens,
                }
            )
            response.raise_for_status()  # Raise HTTP errors as exceptions

            # Check the response structure
            data = response.json()
            if 'choices' not in data or not data['choices']:
                raise ValueError("Invalid response from OpenAI API")

            # Extract the generated text
            generated_text = data['choices'][0]['text']
            return ResponseModel(output=generated_text.strip())

    except ValueError as ve:
        logger.error(f"ValueError: {ve}")
        raise HTTPException(status_code=400, detail=str(ve))
    except httpx.HTTPStatusError as he:
        logger.error(f"HTTP Error {he.response.status_code}: {he.response.text}")
        raise HTTPException(status_code=he.response.status_code, detail="Error during API request")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")