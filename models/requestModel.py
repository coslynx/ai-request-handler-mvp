from typing import Optional
from pydantic import BaseModel, Field, validator
from utils.logger import logger


class RequestModel(BaseModel):
    prompt: str = Field(..., description="Text prompt for AI processing")
    max_tokens: Optional[int] = Field(50, description="Maximum tokens for AI response")

    @validator('prompt')
    def validate_prompt(cls, value):
        if not value.strip():
            logger.error("Validation error: Prompt cannot be empty")
            raise ValueError("Prompt cannot be empty")
        return value