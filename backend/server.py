from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import requests
from transformers import pipeline
import torch
from io import BytesIO
from PIL import Image

app = FastAPI()

# Enable CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load SmolVLM model for image description
device = "cuda" if torch.cuda.is_available() else "cpu"
vlm_pipeline = pipeline("image-to-text", model="HuggingFaceTB/SmolVLM-Instruct", device=device)

@app.get("/")
def home():
    return {"message": "Backend API is running"}

@app.post("/describe-image/")
async def describe_image(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(BytesIO(contents))
    description = vlm_pipeline(image)
    return {"description": description}

@app.post("/process-3d/")
async def process_3d(file: UploadFile = File(...)):
    return {"message": "3D processing with Gaussian Splatting to be implemented"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)

