from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ContentInput(BaseModel):
    brand: str
    niche: str
    audience: str
    platform: str
    goal: str

@app.post("/generate")
def generate_content(data: ContentInput):
    return {
        "message": f"{data.brand} is a {data.niche} brand targeting {data.audience} on {data.platform} with goal {data.goal}"
    }