import os
import shutil
from uuid import uuid4
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from database import engine, Base
from routers.team import router as team_router
from seed import seed

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Armatrix Team API",
    description="REST API for managing Armatrix team members",
    version="1.0.0",
)

# CORS – allow the Next.js frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ensure uploads directory exists
os.makedirs("uploads", exist_ok=True)
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

app.include_router(team_router)

@app.post("/api/upload")
async def upload_image(file: UploadFile = File(...)):
    ext = file.filename.split(".")[-1]
    filename = f"{uuid4()}.{ext}"
    filepath = os.path.join("uploads", filename)
    
    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    return {"url": f"/uploads/{filename}"}


@app.on_event("startup")
def on_startup():
    seed()


@app.get("/")
def root():
    return {"message": "Armatrix Team API is running", "docs": "/docs"}
