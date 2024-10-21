import logging

import uvicorn

from api import router as api_router
from core.config import settings
from create_fastapi_app import create_app

logging.basicConfig(
    level=logging.getLevelNamesMapping()[settings.logging.log_level],
    format=settings.logging.log_format,
)

main_app = create_app(
    create_custom_static_urls=True,
)

main_app.include_router(
    api_router,
)

if __name__ == "__main__":
    uvicorn.run(
        "main:main_app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )
