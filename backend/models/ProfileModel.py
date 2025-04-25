from pydantic import BaseModel, Field
from typing import Optional
from shared.constants import Gender, EmploymentStatus

class ProfileModel(BaseModel):
    age: int = Field(..., ge=0, le=150)
    gender: Gender
    location: str
    employment_status: EmploymentStatus
    work_schedule: Optional[str] = None
    ethnicity: Optional[str] = None

    class Config:
        json_schema_extra = {
            "example": {
                "age": 25,
                "gender": Gender.MALE,
                "location": "Bangladesh",
                "employment_status": EmploymentStatus.EMPLOYED,
                "work_schedule": "9 to 7 job and 2 hour tution and eat and sleep 5 hour.",
                "ethnicity": None
            }
        } 