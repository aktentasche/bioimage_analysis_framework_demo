import ipaddress

import uvicorn  # type: ignore
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from service.router import router

rest_api = FastAPI()
rest_api.include_router(router)


origins = [
    "http://localhost:8080",
]

rest_api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run(  # type: ignore
        # see https://www.uvicorn.org/settings/
        app="service.rest_api:rest_api",
        host=ipaddress.IPv4Address("0.0.0.0").exploded,
        port=51337,
        reload=True,
        log_level="debug",
        workers=8,
    )
