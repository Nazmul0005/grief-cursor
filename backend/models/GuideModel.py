from pydantic import BaseModel, Field
from typing import List, Dict, Optional
from datetime import datetime

class DailyActivity(BaseModel):
    time_period: str
    activity: str
    description: str

class WeeklySchedule(BaseModel):
    monday: List[DailyActivity]
    tuesday: List[DailyActivity]
    wednesday: List[DailyActivity]
    thursday: List[DailyActivity]
    friday: List[DailyActivity]
    saturday: List[DailyActivity]
    sunday: List[DailyActivity]

class ReflectiveQuestion(BaseModel):
    question: str
    context: str
    suggested_prompts: List[str]

class Resource(BaseModel):
    title: str
    description: str
    category: str
    url: Optional[str] = None
    contact: Optional[str] = None

class GuideModel(BaseModel):
    id: str = Field(..., description="Unique identifier for the guide")
    created_at: datetime = Field(default_factory=datetime.now)
    profile_id: str = Field(..., description="Reference to the user's profile")
    detected_mood: str
    mood_emoji: str
    overview: str = Field(..., min_length=100)
    weekly_routine: WeeklySchedule
    reflective_questions: List[ReflectiveQuestion] = Field(..., min_items=3, max_items=5)
    physical_activity: str
    meal_plan: str
    evening_ritual: str
    resources: List[Resource] = Field(..., min_items=1)
    coping_strategies: List[str] = Field(..., min_items=1)
    
    class Config:
        json_schema_extra = {
            "example": {
                "id": "guide_123",
                "profile_id": "user_123",
                "detected_mood": "sad",
                "mood_emoji": "😔",
                "overview": "Based on your recent loss...",
                "weekly_routine": {
                    "monday": [
                        {
                            "time_period": "Morning (9 AM-12 PM)",
                            "activity": "Gentle Exercise",
                            "description": "Start with 10 minutes of stretching..."
                        }
                    ],
                    # ... other days
                },
                "reflective_questions": [
                    {
                        "question": "What memory brings you the most comfort?",
                        "context": "Reflecting on positive memories can help...",
                        "suggested_prompts": [
                            "Think about a time when...",
                            "Remember when you both..."
                        ]
                    }
                ],
                "physical_activity": "Daily 15-minute walks in nature",
                "meal_plan": "Focus on nutritious, easy-to-prepare meals...",
                "evening_ritual": "Create a calming bedtime routine...",
                "resources": [
                    {
                        "title": "Local Grief Support Group",
                        "description": "Weekly meetings for those experiencing loss",
                        "category": "Support Groups",
                        "contact": "555-0123"
                    }
                ],
                "coping_strategies": [
                    "Deep breathing exercises",
                    "Journaling before bed"
                ]
            }
        } 