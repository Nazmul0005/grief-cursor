from fastapi import APIRouter, HTTPException
from models.GuideModel import GuideModel, DailyActivity, WeeklySchedule, ReflectiveQuestion, Resource
from models.AssessmentModel import AssessmentModel
from models.ProfileModel import ProfileModel
from typing import Dict, List
import uuid
from datetime import datetime

router = APIRouter()

# In-memory storage for guides (replace with database in production)
guides: Dict[str, GuideModel] = {}
profile_guides: Dict[str, List[str]] = {}  # Maps profile_id to list of guide_ids

@router.post("/generate-guide", response_model=GuideModel)
async def generate_guide(profile_id: str, assessment_id: str):
    """Generate a personalized grief guide based on profile and assessment"""
    # TODO: Implement guide generation using Groq API
    # This is a placeholder that returns a sample guide
    guide_id = f"guide_{str(uuid.uuid4())}"
    
    guide = GuideModel(
        id=guide_id,
        created_at=datetime.now(),
        profile_id=profile_id,
        detected_mood="sad",
        mood_emoji="😔",
        overview="This is a personalized guide based on your recent loss...",
        weekly_routine=WeeklySchedule(
            monday=[],
            tuesday=[],
            wednesday=[],
            thursday=[],
            friday=[],
            saturday=[],
            sunday=[]
        ),
        reflective_questions=[
            ReflectiveQuestion(
                question="What memory brings you the most comfort?",
                context="Reflecting on positive memories can help in the healing process",
                suggested_prompts=["Think about a happy moment", "Remember a time when you laughed together"]
            )
        ],
        physical_activity="Daily 15-minute walks",
        meal_plan="Focus on nutritious, easy-to-prepare meals",
        evening_ritual="Create a calming bedtime routine",
        resources=[
            Resource(
                title="Local Grief Support Group",
                description="Weekly meetings for those experiencing loss",
                category="Support Groups",
                contact="555-0123"
            )
        ],
        coping_strategies=["Deep breathing", "Journaling"]
    )
    
    guides[guide_id] = guide
    
    if profile_id not in profile_guides:
        profile_guides[profile_id] = []
    profile_guides[profile_id].append(guide_id)
    
    return guide

@router.get("/guide/{guide_id}", response_model=GuideModel)
async def get_guide(guide_id: str):
    """Get a guide by ID"""
    if guide_id not in guides:
        raise HTTPException(status_code=404, detail="Guide not found")
    return guides[guide_id]

@router.get("/guides/profile/{profile_id}", response_model=List[GuideModel])
async def get_profile_guides(profile_id: str):
    """Get all guides for a profile"""
    if profile_id not in profile_guides:
        return []
    
    profile_guide_list = []
    for guide_id in profile_guides[profile_id]:
        if guide_id in guides:
            profile_guide_list.append(guides[guide_id])
    
    return profile_guide_list

@router.delete("/guide/{guide_id}")
async def delete_guide(guide_id: str):
    """Delete a guide"""
    if guide_id not in guides:
        raise HTTPException(status_code=404, detail="Guide not found")
    
    # Remove guide from profile_guides
    for profile_id in profile_guides:
        if guide_id in profile_guides[profile_id]:
            profile_guides[profile_id].remove(guide_id)
    
    del guides[guide_id]
    return {"message": "Guide deleted successfully"} 