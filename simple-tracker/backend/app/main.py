from fastapi import FastAPI
from . import routers
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="API for the live monitoring and analyzing",
    description="API for monitoring and analyzing vehicle traffic. The project is part of the thesis.",
    author="Aleksander Czubiak",
    version="0.1",
    docs_url = "/docs"
)


origins = [
    "https://tracker.toadres.pl/",
    "http://tracker.toadres.pl/"
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routers.router, prefix="", tags=["Endpoints"])