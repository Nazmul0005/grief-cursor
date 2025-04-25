from fastapi import APIRouter, HTTPException
from models.AssessmentModel import AssessmentModel
from services.ProfileManager import ProfileManager
from typing import List

router = APIRouter()
profile_manager = ProfileManager()

@router.post("/profiles/", response_model=AssessmentModel)
async def create_profile(profile: AssessmentModel):
    """
    Create a new profile.
    
    Args:
        profile: The profile data to save
        
    Returns:
        The saved profile data
        
    Raises:
        HTTPException: If there's an error saving the profile
    """
    success = profile_manager.save_profile(profile)
    if not success:
        raise HTTPException(status_code=500, detail="Error saving profile. Please try again.")
    return profile

@router.get("/profiles/", response_model=List[AssessmentModel])
async def get_profiles():
    """
    Get all saved profiles.
    
    Returns:
        List of all saved profiles
    """
    return profile_manager.get_profiles() 