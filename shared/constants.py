from enum import Enum

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

class CauseOfDeath(str, Enum):
    ILLNESS = "Illness"
    ACCIDENT = "Accident"
    AGE = "Age-related"
    SUDDEN = "Sudden/Unexpected"
    SUICIDE = "Suicide"
    OTHER = "Other"

class Relationship(str, Enum):
    PARENT = "Parent"
    CHILD = "Child"
    SPOUSE = "Spouse"
    SIBLING = "Sibling"
    FRIEND = "Friend"
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
    THERAPY = "Professional therapy"
    SUPPORT_GROUP = "Support group"
    RELIGIOUS = "Religious community"
    NONE = "No current support"

class CopingMethod(str, Enum):
    EXERCISE = "Physical exercise"
    MEDITATION = "Meditation"
    JOURNALING = "Journaling"
    ART = "Art or creative expression"
    NATURE = "Spending time in nature"
    WORK = "Focusing on work"
    AVOIDANCE = "Avoiding thoughts about loss"

EMOJI_MOOD_MAP = {
    "devastated": "😢",
    "sad": "😔",
    "anxious": "😰",
    "angry": "😠",
    "numb": "😶",
    "hopeful": "🌱",
    "accepting": "🙏",
    "grateful": "💗",
}

TIME_PERIODS = [
    "Early Morning (6-9 AM)",
    "Morning (9 AM-12 PM)",
    "Afternoon (12-4 PM)",
    "Evening (4-8 PM)",
    "Night (8-11 PM)"
]

REFLECTIVE_PROMPTS = [
    "What memory brings you the most comfort when you think of your loved one?",
    "What would you want to tell them if they were here right now?",
    "How has this loss changed your perspective on life?",
    "What values or lessons from them do you want to carry forward?",
    "What are some ways you can honor their memory in your daily life?",
]

RESOURCE_CATEGORIES = [
    "Professional Support",
    "Support Groups",
    "Reading Materials",
    "Self-Care Activities",
    "Memorial Ideas",
    "Crisis Support"
] 