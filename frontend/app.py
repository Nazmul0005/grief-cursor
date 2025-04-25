import streamlit as st
import requests
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure page
st.set_page_config(
    page_title="Grief Support System",
    page_icon="🕊️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if "profile_id" not in st.session_state:
    st.session_state.profile_id = None
if "current_page" not in st.session_state:
    st.session_state.current_page = "home"
if "assessment_id" not in st.session_state:
    st.session_state.assessment_id = None
if "guide_history" not in st.session_state:
    st.session_state.guide_history = []

# API configuration
API_BASE_URL = "http://localhost:8000/api/v1"

def get_emoji_for_mood(mood: str) -> str:
    emoji_map = {
        "devastated": "😢",
        "sad": "😔",
        "anxious": "😰",
        "angry": "😠",
        "numb": "😶",
        "hopeful": "🌱",
        "accepting": "🙏",
        "grateful": "💗",
    }
    return emoji_map.get(mood, "😔")

def display_navigation():
    """Display the navigation bar"""
    cols = st.columns([1, 2, 1])
    
    with cols[0]:
        if st.button("🏠 Home"):
            st.session_state.current_page = "home"
            st.rerun()
    
    with cols[1]:
        st.title("Grief Support System")
    
    with cols[2]:
        if st.session_state.profile_id:
            if st.button("👤 Profile"):
                st.session_state.current_page = "profile"
                st.rerun()

def display_home():
    """Display the home page"""
    st.write("## Welcome to Your Grief Support Journey")
    st.write("""
    This platform provides personalized support for your grief journey through:
    - Custom weekly routines
    - Reflective exercises
    - Resource recommendations
    - Mood tracking
    """)
    
    if st.button("Start Your Journey", type="primary"):
        st.session_state.current_page = "profile"
        st.rerun()

def display_profile():
    """Display the profile creation/edit page"""
    st.write("## Your Profile")
    
    with st.form("profile_form"):
        name = st.text_input("Name")
        age = st.number_input("Age", min_value=13, max_value=120)
        gender = st.selectbox("Gender", ["Male", "Female", "Non-binary", "Other"])
        location = st.text_input("Location")
        employment = st.selectbox("Employment Status", 
                                ["Employed", "Unemployed", "Student", "Retired", "Other"])
        schedule = st.text_area("Work/Daily Schedule (optional)")
        ethnicity = st.text_input("Ethnicity (optional)")
        
        if st.form_submit_button("Save Profile"):
            profile_data = {
                "name": name,
                "age": age,
                "gender": gender,
                "location": location,
                "employment_status": employment,
                "work_schedule": schedule,
                "ethnicity": ethnicity
            }
            
            response = requests.post(f"{API_BASE_URL}/profile", json=profile_data)
            if response.status_code == 200:
                st.session_state.profile_id = response.json()["profile_id"]
                st.success("Profile saved successfully!")
                st.session_state.current_page = "assessment"
                st.rerun()
            else:
                st.error("Error saving profile. Please try again.")

def main():
    """Main application logic"""
    display_navigation()
    
    if st.session_state.current_page == "home":
        display_home()
    elif st.session_state.current_page == "profile":
        display_profile()
    # Other pages will be imported from the pages directory
    
    # Display guide history in sidebar if available
    if st.session_state.guide_history:
        with st.sidebar:
            st.write("## Your Guide History")
            for guide in st.session_state.guide_history:
                with st.expander(f"{get_emoji_for_mood(guide['detected_mood'])} {guide['created_at'][:10]}"):
                    st.write(guide['overview'][:100] + "...")
                    if st.button("View Guide", key=guide['id']):
                        st.session_state.current_guide = guide
                        st.session_state.current_page = "guide"
                        st.rerun()

if __name__ == "__main__":
    main() 