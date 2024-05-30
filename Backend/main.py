from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
import json
import markdown

app = FastAPI()
secretcode = "By Z44k1R_D3V"

# Define allowed origins
origins = [
    "http://127.0.0.1:5500",
    # Add other origins if necessary
]

# Add CORS middleware to the FastAPI app
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class prompt(BaseModel):
    tech: str

def ask(input: str):
    url = "http://localhost:11434/api/generate"
    headers = {
        'content-type': 'application/json',
    }
    data = {
        "model": "llama3",
        "prompt": input,
        "stream": False
    }
    resp = requests.post(url=url, headers=headers, data=json.dumps(data))
    response_json = resp.json()
    return response_json.get("response")

@app.post("/generate")
def Generate(Prompt: prompt):
    instruction= f"Create a long and easy to understand tutorial on how to use {Prompt.tech}. Please return the document response as html but only the body and without the <body><body/> tags."
    r = ask(instruction)
    clean_response = r.replace('\n', ' ').strip()
    return clean_response
