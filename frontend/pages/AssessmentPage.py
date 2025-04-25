import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

import streamlit as st
import requests
from shared.constants import (
    Relationship,
    CauseOfDeath,
    TimeSinceLoss,
    SupportSystem,
    CopingMethod,
    Gender,
    EmploymentStatus,
    EMOJI_MOOD_MAP
)

def display_assessment():
    st.markdown("""
    <style>
    .big-font {
        font-size:24px !important;
        font-weight: bold;
    }
    .stProgress > div > div > div > div {
        background-color: #ff4b4b;
    }
    </style>
    """, unsafe_allow_html=True)

    # Header with progress
    st.markdown('<p class="big-font">Grief Assessment & Support Guide</p>', unsafe_allow_html=True)
    st.write("We're here to help you through your journey. Take your time with each question.")
    
    # Calculate progress
    total_steps = 5
    current_step = st.session_state.get('assessment_step', 1)
    progress = (current_step - 1) / total_steps
    st.progress(progress)
    
    # Initialize session state
    if 'assessment_step' not in st.session_state:
        st.session_state.assessment_step = 1
        st.session_state.temp_assessment = {}
    
    # Display current step
    if st.session_state.assessment_step == 1:
        display_profile_step()
    elif st.session_state.assessment_step == 2:
        display_loss_info_step()
    elif st.session_state.assessment_step == 3:
        display_support_step()
    elif st.session_state.assessment_step == 4:
        display_wellbeing_step()
    elif st.session_state.assessment_step == 5:
        display_story_step()

def display_profile_step():
    """Step 1: Basic Profile Information"""
    st.write("### 📋 Your Profile")
    st.write("This information helps us provide more personalized support.")
    
    with st.form("profile_step"):
        col1, col2 = st.columns(2)
        
        with col1:
            age = st.number_input("Age", min_value=0, max_value=150, value=25)
            gender = st.selectbox("Gender", [g.value for g in Gender])
            location = st.text_input("Location")
        
        with col2:
            employment_status = st.selectbox("Employment Status", [e.value for e in EmploymentStatus])
            work_schedule = st.text_area("Daily Schedule (optional)", 
                                       help="Brief description of your typical day",
                                       placeholder="E.g., Work hours, routines, commitments")
            ethnicity = st.text_input("Ethnicity (optional)")
        
        submit = st.form_submit_button("Continue →")
        if submit:
            if not location:
                st.error("Please enter your location.")
                return
                
            profile_data = {
                "age": age,
                "gender": gender,
                "location": location,
                "employment_status": employment_status,
                "work_schedule": work_schedule if work_schedule else None,
                "ethnicity": ethnicity if ethnicity else None
            }
            
            try:
                response = requests.post(
                    "http://localhost:8000/api/v1/profile",
                    json=profile_data
                )
                if response.status_code == 200:
                    st.session_state.profile_id = response.json()["profile_id"]
                    st.session_state.assessment_step = 2
                    st.rerun()
                else:
                    st.error("Error saving profile. Please try again.")
            except Exception as e:
                st.error(f"Connection error. Please check if the server is running.")

def display_loss_info_step():
    """Step 2: Loss Information"""
    st.write("### 💝 About Your Loss")
    st.write("We understand this may be difficult. Take your time to answer.")
    
    with st.form("loss_info_step"):
        col1, col2 = st.columns(2)
        
        with col1:
            relationship = st.selectbox(
                "What was your relationship to the person you lost?",
                [r.value for r in Relationship],
                help="Select the option that best describes your relationship"
            )
            
            cause = st.selectbox(
                "What was the cause of loss?",
                [c.value for c in CauseOfDeath],
                help="Select the primary cause"
            )
        
        with col2:
            time_since = st.selectbox(
                "How long has it been since your loss?",
                [t.value for t in TimeSinceLoss],
                help="Select the approximate time period"
            )
        
        col_back, col_space, col_next = st.columns([1, 2, 1])
        with col_back:
            if st.form_submit_button("← Back"):
                st.session_state.assessment_step = 1
                st.rerun()
        with col_next:
            if st.form_submit_button("Continue →"):
                st.session_state.temp_assessment.update({
                    "relationship": relationship,
                    "cause_of_death": cause,
                    "time_since_loss": time_since
                })
                st.session_state.assessment_step = 3
                st.rerun()

def display_support_step():
    """Step 3: Support Systems"""
    st.write("### 🤝 Support & Coping")
    st.write("Understanding your support system helps us provide better recommendations.")
    
    with st.form("support_step"):
        col1, col2 = st.columns(2)
        
        with col1:
            current_support = st.multiselect(
                "What support systems do you currently have?",
                [s.value for s in SupportSystem],
                help="Select all that apply"
            )
        
        with col2:
            coping_methods = st.multiselect(
                "What methods are you using to cope with your loss?",
                [m.value for m in CopingMethod],
                help="Select all that apply"
            )
        
        col_back, col_space, col_next = st.columns([1, 2, 1])
        with col_back:
            if st.form_submit_button("← Back"):
                st.session_state.assessment_step = 2
                st.rerun()
        with col_next:
            if st.form_submit_button("Continue →"):
                if not current_support or not coping_methods:
                    st.error("Please select at least one option for each question.")
                    return
                    
                st.session_state.temp_assessment.update({
                    "current_support": current_support,
                    "coping_methods": coping_methods
                })
                st.session_state.assessment_step = 4
                st.rerun()

def display_wellbeing_step():
    """Step 4: Current Wellbeing"""
    st.write("### 🌱 Your Current Wellbeing")
    st.write("This helps us understand how you're doing right now.")
    
    with st.form("wellbeing_step"):
        col1, col2 = st.columns(2)
        
        with col1:
            sleep_quality = st.slider(
                "How would you rate your sleep quality?",
                1, 5, 3,
                help="1 = Very poor, 5 = Very good"
            )
            
            energy_level = st.slider(
                "How would you rate your energy level?",
                1, 5, 3,
                help="1 = Very low, 5 = Very high"
            )
            
            appetite_changes = st.checkbox(
                "Have you noticed changes in your appetite?",
                help="Check if you've experienced significant changes in eating patterns"
            )
        
        with col2:
            social_withdrawal = st.checkbox(
                "Have you been withdrawing from social interactions?",
                help="Check if you've been avoiding social situations more than usual"
            )
            
            difficulty_concentrating = st.checkbox(
                "Are you having difficulty concentrating?",
                help="Check if you're finding it hard to focus on tasks"
            )
            
            physical_symptoms = st.multiselect(
                "Are you experiencing any physical symptoms?",
                ["Headaches", "Fatigue", "Chest pain", "Muscle tension", "Digestive issues", "None"],
                help="Select all that apply"
            )
        
        col_back, col_space, col_next = st.columns([1, 2, 1])
        with col_back:
            if st.form_submit_button("← Back"):
                st.session_state.assessment_step = 3
                st.rerun()
        with col_next:
            if st.form_submit_button("Continue →"):
                st.session_state.temp_assessment.update({
                    "sleep_quality": sleep_quality,
                    "appetite_changes": appetite_changes,
                    "energy_level": energy_level,
                    "social_withdrawal": social_withdrawal,
                    "difficulty_concentrating": difficulty_concentrating,
                    "physical_symptoms": [s for s in physical_symptoms if s != "None"]
                })
                st.session_state.assessment_step = 5
                st.rerun()

def display_story_step():
    """Step 5: Personal Story"""
    st.write("### 📝 Your Story")
    st.write("Sharing your story can be therapeutic. Take your time to express your thoughts and feelings.")
    
    with st.form("story_step"):
        story = st.text_area(
            "What would you like to share about your loss and how you're feeling?",
            height=200,
            help="This is a safe space to express yourself. Your story helps us understand your unique experience.",
            placeholder="You can write about your memories, feelings, challenges, or anything else you'd like to share..."
        )
        
        col_back, col_space, col_submit = st.columns([1, 2, 1])
        with col_back:
            if st.form_submit_button("← Back"):
                st.session_state.assessment_step = 4
                st.rerun()
        with col_submit:
            if st.form_submit_button("Create Support Guide"):
                if len(story.strip()) < 50:
                    st.error("Please share a bit more about your experience (minimum 50 characters)")
                    return
                
                st.session_state.temp_assessment["story"] = story
                
                try:
                    # Submit assessment
                    response = requests.post(
                        "http://localhost:8000/api/v1/assessment",
                        json=st.session_state.temp_assessment,
                        params={"profile_id": st.session_state.profile_id}
                    )
                    
                    if response.status_code == 200:
                        assessment_id = response.json()["assessment_id"]
                        st.session_state.assessment_id = assessment_id
                        
                        # Generate guide
                        guide_response = requests.post(
                            "http://localhost:8000/api/v1/generate-guide",
                            params={
                                "profile_id": st.session_state.profile_id,
                                "assessment_id": assessment_id
                            }
                        )
                        
                        if guide_response.status_code == 200:
                            guide = guide_response.json()
                            st.session_state.current_guide = guide
                            if "guide_history" not in st.session_state:
                                st.session_state.guide_history = []
                            st.session_state.guide_history.append(guide)
                            st.session_state.current_page = "guide"
                            st.rerun()
                        else:
                            st.error("Error generating your support guide. Please try again.")
                    else:
                        st.error("Error saving your assessment. Please try again.")
                except Exception as e:
                    st.error("Connection error. Please check if the server is running.") 