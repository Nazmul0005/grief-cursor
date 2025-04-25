from groq import Groq
from models.ProfileModel import ProfileModel
from models.AssessmentModel import AssessmentModel
from models.GuideModel import GuideModel, DailyRoutine, WeeklySchedule, ReflectiveQuestion, Resource
from shared.constants import EMOJI_MOOD_MAP, TIME_PERIODS, REFLECTIVE_PROMPTS, RESOURCE_CATEGORIES
import os
from typing import Dict, List
import json

class GroqService:
    def __init__(self):
        self.client = Groq(
            api_key=os.getenv("GROQ_API_KEY", "your-api-key-here")
        )
        self.model = "mixtral-8x7b-32768"  # Using Mixtral for its strong reasoning capabilities
    
    async def analyze_mood(self, text: str) -> Dict[str, str]:
        """Analyze the emotional state from text"""
        prompt = f"""Analyze the emotional state in this text and categorize it into one of these moods: devastated, sad, anxious, angry, numb, hopeful, accepting, grateful. Return only the mood word.

Text: {text}"""
        
        response = await self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        
        mood = response.choices[0].message.content.strip().lower()
        return {
            "mood": mood,
            "emoji": EMOJI_MOOD_MAP.get(mood, "😔")
        }
    
    async def generate_guide(self, profile: ProfileModel, assessment: AssessmentModel) -> GuideModel:
        """Generate a personalized grief guide"""
        # Generate overview
        overview_prompt = self._create_overview_prompt(profile, assessment)
        overview_response = await self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": overview_prompt}]
        )
        overview = overview_response.choices[0].message.content.strip()
        
        # Generate weekly routine
        routine_prompt = self._create_routine_prompt(profile, assessment)
        routine_response = await self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": routine_prompt}]
        )
        weekly_routine = self._parse_routine_response(routine_response.choices[0].message.content)
        
        # Generate reflective questions
        questions_prompt = self._create_questions_prompt(assessment)
        questions_response = await self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": questions_prompt}]
        )
        reflective_questions = self._parse_questions_response(questions_response.choices[0].message.content)
        
        # Generate resources
        resources_prompt = self._create_resources_prompt(profile, assessment)
        resources_response = await self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": resources_prompt}]
        )
        resources = self._parse_resources_response(resources_response.choices[0].message.content)
        
        # Analyze mood from story
        mood_analysis = await self.analyze_mood(assessment.story)
        
        return GuideModel(
            id="temp_id",  # Will be replaced when saved
            profile_id="temp_profile_id",  # Will be replaced when saved
            detected_mood=mood_analysis["mood"],
            mood_emoji=mood_analysis["emoji"],
            overview=overview,
            weekly_routine=weekly_routine,
            reflective_questions=reflective_questions,
            physical_activity=self._generate_physical_activity(assessment),
            meal_plan=self._generate_meal_plan(assessment),
            evening_ritual=self._generate_evening_ritual(assessment),
            resources=resources,
            coping_strategies=self._generate_coping_strategies(assessment)
        )
    
    def _create_overview_prompt(self, profile: ProfileModel, assessment: AssessmentModel) -> str:
        return f"""Create a compassionate and personalized overview for someone grieving. Consider:
- They lost their {assessment.relationship.value}
- Cause: {assessment.cause_of_death.value}
- Time since loss: {assessment.time_since_loss.value}
- Current support: {', '.join([s.value for s in assessment.current_support])}
- Their story: {assessment.story}

Write a 2-3 paragraph overview that validates their feelings and offers hope."""
    
    def _create_routine_prompt(self, profile: ProfileModel, assessment: AssessmentModel) -> str:
        return f"""Create a structured weekly routine for someone grieving. Consider:
- Their work schedule: {profile.work_schedule}
- Their energy level: {assessment.energy_level}/5
- Their sleep quality: {assessment.sleep_quality}/5
- Their current coping methods: {', '.join([m.value for m in assessment.coping_methods])}

Return the routine as a JSON object with days of the week as keys, and arrays of activities for each time period."""
    
    def _create_questions_prompt(self, assessment: AssessmentModel) -> str:
        return f"""Generate 3 reflective questions that would be helpful for someone who:
- Lost their {assessment.relationship.value}
- Is experiencing grief for {assessment.time_since_loss.value}
- Has these coping methods: {', '.join([m.value for m in assessment.coping_methods])}

Return as a JSON array of question objects with 'question', 'context', and 'suggested_prompts' fields."""
    
    def _create_resources_prompt(self, profile: ProfileModel, assessment: AssessmentModel) -> str:
        return f"""Suggest grief support resources for someone who:
- Lives in {profile.location}
- Lost their {assessment.relationship.value}
- Has support from: {', '.join([s.value for s in assessment.current_support])}

Return as a JSON array of resource objects with 'title', 'description', 'category', and optional 'contact' fields."""
    
    def _parse_routine_response(self, response: str) -> WeeklySchedule:
        try:
            data = json.loads(response)
            return WeeklySchedule(**data)
        except:
            # Return a basic schedule if parsing fails
            return WeeklySchedule(
                monday=[],
                tuesday=[],
                wednesday=[],
                thursday=[],
                friday=[],
                saturday=[],
                sunday=[]
            )
    
    def _parse_questions_response(self, response: str) -> List[ReflectiveQuestion]:
        try:
            data = json.loads(response)
            return [ReflectiveQuestion(**q) for q in data]
        except:
            # Return default questions if parsing fails
            return [
                ReflectiveQuestion(
                    question=REFLECTIVE_PROMPTS[0],
                    context="This question helps process memories",
                    suggested_prompts=["Think about...", "Remember when..."]
                )
            ]
    
    def _parse_resources_response(self, response: str) -> List[Resource]:
        try:
            data = json.loads(response)
            return [Resource(**r) for r in data]
        except:
            # Return a default resource if parsing fails
            return [
                Resource(
                    title="Grief Support Hotline",
                    description="24/7 support line for those experiencing grief",
                    category="Crisis Support",
                    contact="1-800-XXX-XXXX"
                )
            ]
    
    def _generate_physical_activity(self, assessment: AssessmentModel) -> str:
        if assessment.energy_level <= 2:
            return "Gentle stretching and short walks"
        elif assessment.energy_level <= 4:
            return "Daily 15-minute walks and light yoga"
        else:
            return "Regular exercise including walks, yoga, or your preferred physical activity"
    
    def _generate_meal_plan(self, assessment: AssessmentModel) -> str:
        if assessment.appetite_changes:
            return "Start with small, frequent meals. Focus on nutritious, easy-to-digest foods."
        else:
            return "Maintain regular meal times with balanced nutrition."
    
    def _generate_evening_ritual(self, assessment: AssessmentModel) -> str:
        components = []
        if assessment.sleep_quality <= 3:
            components.extend([
                "Create a calm environment 1 hour before bed",
                "Practice deep breathing or gentle stretching",
                "Avoid screens 30 minutes before sleep"
            ])
        if CopingMethod.JOURNALING in assessment.coping_methods:
            components.append("Write in your journal")
        if CopingMethod.MEDITATION in assessment.coping_methods:
            components.append("Practice a short meditation")
            
        return " ".join(components) if components else "Develop a consistent bedtime routine"
    
    def _generate_coping_strategies(self, assessment: AssessmentModel) -> List[str]:
        strategies = []
        for method in assessment.coping_methods:
            if method == CopingMethod.EXERCISE:
                strategies.append("Regular physical activity")
            elif method == CopingMethod.MEDITATION:
                strategies.append("Daily meditation practice")
            elif method == CopingMethod.JOURNALING:
                strategies.append("Express feelings through writing")
            elif method == CopingMethod.ART:
                strategies.append("Creative expression through art")
            elif method == CopingMethod.NATURE:
                strategies.append("Time in nature")
        
        # Add general strategies
        strategies.extend([
            "Deep breathing exercises",
            "Connecting with others",
            "Self-compassion practice"
        ])
        
        return strategies[:5]  # Return top 5 strategies 