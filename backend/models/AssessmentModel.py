import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from pydantic import BaseModel, Field
from typing import List, Optional
from shared.constants import (
    Relationship,
    CauseOfDeath,
    TimeSinceLoss,
    SupportSystem,
    CopingMethod,
    Gender,
    EmploymentStatus
)

class AssessmentModel(BaseModel):
    # Basic profile information
    age: int = Field(..., ge=0, le=150)
    gender: Gender
    location: str
    employment_status: EmploymentStatus
    work_schedule: Optional[str] = None
    ethnicity: Optional[str] = None

    # Grief assessment fields
    relationship: Relationship
    cause_of_death: CauseOfDeath
    time_since_loss: TimeSinceLoss
    current_support: List[SupportSystem]
    coping_methods: List[CopingMethod]
    sleep_quality: int = Field(..., ge=1, le=5)  # 1-5 scale
    appetite_changes: bool
    energy_level: int = Field(..., ge=1, le=5)  # 1-5 scale
    social_withdrawal: bool
    difficulty_concentrating: bool
    physical_symptoms: List[str]
    story: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "age": 25,
                "gender": Gender.MALE,
                "location": "Bangladesh",
                "employment_status": EmploymentStatus.EMPLOYED,
                "work_schedule": "9 to 7 job and 2 hour tution and eat and sleep 5 hour.",
                "ethnicity": None,
                "cause_of_death": CauseOfDeath.ILLNESS,
                "relationship": Relationship.PARENT,
                "time_since_loss": TimeSinceLoss.MONTHS,
                "current_support": [SupportSystem.FAMILY, SupportSystem.FRIENDS],
                "coping_methods": [CopingMethod.EXERCISE, CopingMethod.MEDITATION],
                "story": "My father passed away three months ago...",
                "sleep_quality": 3,
                "appetite_changes": True,
                "energy_level": 2,
                "social_withdrawal": True,
                "difficulty_concentrating": True,
                "physical_symptoms": ["headaches", "fatigue"]
            }
        } 