from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.assessment_router import router as assessment_router
from routers.guide_router import router as guide_router
from routers.profile_router import router as profile_router
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Create FastAPI app
app = FastAPI(
    title="Grief Support System API",
    description="API for personalized grief support and guide generation",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8501"],  # Streamlit frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(profile_router, prefix="/api/v1", tags=["profiles"])
app.include_router(assessment_router, prefix="/api/v1", tags=["assessments"])
app.include_router(guide_router, prefix="/api/v1", tags=["guides"])

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Welcome to the Grief Support System API",
        "docs_url": "/docs",
        "redoc_url": "/redoc"
    }

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    ) 