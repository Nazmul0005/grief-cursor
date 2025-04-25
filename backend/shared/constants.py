from enum import Enum

class Relationship(str, Enum):
    PARENT = "Parent"
    CHILD = "Child"
    SPOUSE = "Spouse"
    SIBLING = "Sibling"
    FRIEND = "Friend"
    GRANDPARENT = "Grandparent"
    OTHER = "Other"

class CauseOfDeath(str, Enum):
    ILLNESS = "Illness"
    ACCIDENT = "Accident"
    AGE = "Age-related"
    SUDDEN = "Sudden/Unexpected"
    SUICIDE = "Suicide"
    OTHER = "Other"

class TimeSinceLoss(str, Enum):
    DAYS = "Less than a week"
    WEEKS = "Weeks"
    MONTHS = "Months"
    YEAR = "About a year"
    YEARS = "Multiple years"

class SupportSystem(str, Enum):
    FAMILY = "Family"
    FRIENDS = "Friends"
    THERAPIST = "Professional therapist"
    SUPPORT_GROUP = "Support group"
    RELIGIOUS = "Religious/Spiritual community"
    NONE = "No current support"

class CopingMethod(str, Enum):
    EXERCISE = "Exercise"
    MEDITATION = "Meditation"
    JOURNALING = "Journaling"
    ART = "Art/Creative expression"
    NATURE = "Time in nature"
    WORK = "Work/Keeping busy"
    TALKING = "Talking with others"
    NONE = "No specific methods"

class Gender(str, Enum):
    MALE = "Male"
    FEMALE = "Female"
    OTHER = "Other"
    PREFER_NOT_TO_SAY = "Prefer not to say"

class EmploymentStatus(str, Enum):
    EMPLOYED = "Employed"
    UNEMPLOYED = "Unemployed"
    STUDENT = "Student"
    RETIRED = "Retired"
    OTHER = "Other"

EMOJI_MOOD_MAP = {
    "devastated": "😢",
    "sad": "😔",
    "anxious": "😰",
    "angry": "😠",
    "numb": "😶",
    "hopeful": "🌱",
    "accepting": "🙏",
    "grateful": "💗"
}

TIME_PERIODS = [
    "Early morning",
    "Morning",
    "Late morning",
    "Noon",
    "Early afternoon",
    "Afternoon",
    "Late afternoon",
    "Evening",
    "Night"
]

REFLECTIVE_PROMPTS = [
    "What memory brings you the most comfort?",
    "How has this loss changed your perspective?",
    "What would you want them to know?",
    "What are you grateful for in your relationship?",
    "How have you grown through this experience?",
    "What helps you feel connected to them?"
]

RESOURCE_CATEGORIES = [
    "Support Groups",
    "Professional Support",
    "Crisis Support",
    "Self-Care Activities",
    "Educational Resources",
    "Community Services"
] 