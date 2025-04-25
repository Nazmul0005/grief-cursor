from fastapi import APIRouter, HTTPException
from models.ProfileModel import ProfileModel
from typing import Dict
import uuid

router = APIRouter()

# In-memory storage for profiles (replace with database in production)
profiles: Dict[str, ProfileModel] = {}

@router.post("/profile", response_model=Dict[str, str])
async def create_profile(profile: ProfileModel):
    """Create a new user profile"""
    profile_id = f"profile_{str(uuid.uuid4())}"
    profiles[profile_id] = profile
    return {"profile_id": profile_id}

@router.get("/profile/{profile_id}", response_model=ProfileModel)
async def get_profile(profile_id: str):
    """Get a user profile by ID"""
    if profile_id not in profiles:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profiles[profile_id]

@router.put("/profile/{profile_id}", response_model=ProfileModel)
async def update_profile(profile_id: str, profile: ProfileModel):
    """Update a user profile"""
    if profile_id not in profiles:
        raise HTTPException(status_code=404, detail="Profile not found")
    profiles[profile_id] = profile
    return profile

@router.delete("/profile/{profile_id}")
async def delete_profile(profile_id: str):
    """Delete a user profile"""
    if profile_id not in profiles:
        raise HTTPException(status_code=404, detail="Profile not found")
    del profiles[profile_id]
    return {"message": "Profile deleted successfully"} 