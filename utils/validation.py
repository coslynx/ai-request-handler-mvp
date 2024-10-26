from pydantic import BaseModel, Field, validator
from typing import Optional
from utils.logger import logger

class ValidationError(Exception):
    """Custom exception for validation errors."""
    pass

class RequestModel(BaseModel):
    prompt: str = Field(..., description="Text prompt for AI processing")
    max_tokens: Optional[int] = Field(50, description="Maximum tokens for AI response")

    @validator('prompt')
    def validate_prompt(cls, value):
        if not value.strip():
            logger.error("Validation error: Prompt cannot be empty")
            raise ValidationError("Prompt cannot be empty")
        return value

    @validator('max_tokens')
    def validate_max_tokens(cls, value):
        if value <= 0:
            logger.error("Validation error: Max tokens must be a positive integer")
            raise ValidationError("Max tokens must be a positive integer")
        return value

def validate_request(data: RequestModel) -> bool:
    """Validate incoming request data."""
    try:
        data.prompt = validate_prompt(data.prompt)
        data.max_tokens = validate_max_tokens(data.max_tokens)
    except ValidationError as e:
        logger.error(f"Validation failed: {e}")
        raise
    return True