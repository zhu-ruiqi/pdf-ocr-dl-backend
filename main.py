from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS config to allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to specific domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload_pdf")
async def upload_pdf(file: UploadFile = File(...)):
    content = await file.read()
    simulated_result = f"Simulated OCR result from file: {file.filename}"
    return {"text": simulated_result}
