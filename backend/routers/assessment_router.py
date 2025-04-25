from fastapi import APIRouter, HTTPException
from models.AssessmentModel import AssessmentModel
from typing import Dict, List
import uuid

router = APIRouter()

# In-memory storage for assessments (replace with database in production)
assessments: Dict[str, AssessmentModel] = {}
profile_assessments: Dict[str, List[str]] = {}  # Maps profile_id to list of assessment_ids

@router.post("/assessment", response_model=Dict[str, str])
async def create_assessment(assessment: AssessmentModel, profile_id: str):
    """Create a new grief assessment"""
    assessment_id = f"assessment_{str(uuid.uuid4())}"
    assessments[assessment_id] = assessment
    
    if profile_id not in profile_assessments:
        profile_assessments[profile_id] = []
    profile_assessments[profile_id].append(assessment_id)
    
    return {"assessment_id": assessment_id}

@router.get("/assessment/{assessment_id}", response_model=AssessmentModel)
async def get_assessment(assessment_id: str):
    """Get an assessment by ID"""
    if assessment_id not in assessments:
        raise HTTPException(status_code=404, detail="Assessment not found")
    return assessments[assessment_id]

@router.get("/assessments/profile/{profile_id}", response_model=List[AssessmentModel])
async def get_profile_assessments(profile_id: str):
    """Get all assessments for a profile"""
    if profile_id not in profile_assessments:
        return []
    
    profile_assessment_list = []
    for assessment_id in profile_assessments[profile_id]:
        if assessment_id in assessments:
            profile_assessment_list.append(assessments[assessment_id])
    
    return profile_assessment_list

@router.post("/analyze-mood")
async def analyze_mood(text: str):
    """Analyze the emotional state from text"""
    # TODO: Implement mood analysis using Groq API
    # This is a placeholder that returns a default mood
    return {
        "mood": "sad",
        "emoji": "😔",
        "confidence": 0.8
    } 