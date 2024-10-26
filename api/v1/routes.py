from fastapi import APIRouter, HTTPException
from api.v1.controllers.aiController import handle_ai_request
from models.requestModel import RequestModel
from models.responseModel import ResponseModel

router = APIRouter()

@router.post('/ai/request', response_model=ResponseModel)
async def post_request(request: RequestModel):
    try:
        response = await handle_ai_request(request)
        return response
    except ValueError as err:
        raise HTTPException(status_code=400, detail=str(err))
    except Exception as err:
        raise HTTPException(status_code=500, detail="Internal server error")

@router.get('/health', response_model=dict)
async def health_check():
    return {"status": "healthy"}