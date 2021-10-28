from fastapi import FastAPI
from . import routers

app = FastAPI(
    title="API for the live monitoring and analyzing",
    description="API for monitoring and analyzing vehicle traffic. The project is part of the thesis.",
    author="Aleksander Czubiak",
    version="0.1",
    docs_url = "/docs"
)

app.include_router(routers.router, prefix="", tags=["Endpoints"])