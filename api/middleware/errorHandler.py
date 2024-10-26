from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
import logging

logger = logging.getLogger("errorHandler")

async def error_handling_middleware(request: Request, call_next):
    try:
        response = await call_next(request)
        if response.status_code == 422:
            logger.warning("Validation error during request processing")
            raise HTTPException(status_code=422, detail="Validation Failed")
        return response
    except HTTPException as http_error:
        logger.error(f"HTTP Error: {http_error.detail}")
        return JSONResponse(status_code=http_error.status_code, content={"detail": http_error.detail})
    except Exception as err:
        logger.exception("Unhandled Exception")
        return JSONResponse(status_code=500, content={"detail": "Internal Server Error"})