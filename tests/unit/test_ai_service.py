import pytest
from unittest.mock import patch
from services.aiService import handle_ai_request
from models.requestModel import RequestModel
from models.responseModel import ResponseModel
from fastapi import HTTPException

class TestAIService:

    @patch("httpx.AsyncClient.post")
    async def test_handle_ai_request_valid_input(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {
            "choices": [{"text": "Generated response"}]
        }

        request_data = RequestModel(prompt="Hello, AI!", max_tokens=50)
        response = await handle_ai_request(request_data)

        assert isinstance(response, ResponseModel)
        assert response.output == "Generated response"

    async def test_handle_ai_request_invalid_prompt(self):
        request_data = RequestModel(prompt="", max_tokens=50)
        with pytest.raises(HTTPException) as exc_info:
            await handle_ai_request(request_data)
        
        assert exc_info.value.status_code == 400
        assert "Prompt cannot be empty" in str(exc_info.value.detail)

    @patch("httpx.AsyncClient.post")
    async def test_handle_ai_request_api_failure(self, mock_post):
        mock_post.side_effect = HTTPException(status_code=500, detail="Internal Server Error")

        request_data = RequestModel(prompt="Test", max_tokens=50)
        with pytest.raises(HTTPException) as exc_info:
            await handle_ai_request(request_data)

        assert exc_info.value.status_code == 500
        assert "Error during API request" in str(exc_info.value.detail)