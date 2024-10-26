from fastapi import APIRouter, HTTPException
from models.requestModel import RequestModel
from models.responseModel import ResponseModel
import httpx
import os
from utils.logger import logger

router = APIRouter()

@router.post('/ai/request', response_model=ResponseModel)
async def handle_ai_request(request: RequestModel):
    try:
        # Validate incoming request
        if not request.prompt:
            raise ValueError("Prompt cannot be empty")

        async with httpx.AsyncClient() as client:
            response = await client.post(
                "https://api.openai.com/v1/engines/davinci/completions",
                headers={"Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}",
                         "Content-Type": "application/json"},
                json={
                    "prompt": request.prompt,
                    "max_tokens": request.max_tokens,
                }
            )
            
            response.raise_for_status()  # Raise for HTTP errors

            data = response.json()
            if 'choices' not in data or not data['choices']:
                raise ValueError("Invalid response from OpenAI API")

            generated_text = data['choices'][0]['text']
            return ResponseModel(output=generated_text.strip())
        
    except ValueError as err:
        logger.error(f"ValueError: {err}")
        raise HTTPException(status_code=400, detail=str(err))
    except httpx.HTTPStatusError as http_err:
        logger.error(f"HTTPError: {http_err.response.status_code} - {http_err.response.text}")
        raise HTTPException(status_code=http_err.response.status_code, detail="Error during API request")
    except Exception as err:
        logger.error(f"Unexpected error: {err}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.get('/health', response_model=dict)
async def health_check():
    return {"status": "healthy"}