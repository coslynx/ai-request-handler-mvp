from pydantic import BaseModel, Field
from typing import Optional

class ResponseModel(BaseModel):
    output: str = Field(..., description="The response output from the AI model")
    status_code: int = Field(default=200, description="HTTP status code of the response")
    message: Optional[str] = Field(default=None, description="Additional message for the user")
    
    def to_json(self):
        return {
            "output": self.output,
            "status_code": self.status_code,
            "message": self.message,
        }