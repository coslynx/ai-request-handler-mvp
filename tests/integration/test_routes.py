import os
import pytest
from fastapi.testclient import TestClient
from main import app
from models.requestModel import RequestModel
from models.responseModel import ResponseModel

client = TestClient(app)

def test_post_ai_request_valid_payload():
    valid_payload = {
        "prompt": "Hello, AI!",
        "max_tokens": 50
    }
    response = client.post("/ai/request", json=valid_payload)
    
    assert response.status_code == 200
    response_data = ResponseModel(**response.json())
    assert isinstance(response_data, ResponseModel)
    assert response_data.output is not None

def test_post_ai_request_invalid_payload():
    invalid_payload = {
        "prompt": "",
        "max_tokens": 50
    }
    response = client.post("/ai/request", json=invalid_payload)
    
    assert response.status_code == 400
    assert "Prompt cannot be empty" in response.json()["detail"]

def test_health_check():
    response = client.get("/health")
    
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}