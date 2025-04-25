import streamlit as st
from datetime import datetime

def display_navigation_bar():
    """Display the navigation bar with mood and user info"""
    with st.container():
        # Create three columns for navigation
        left_col, center_col, right_col = st.columns([1, 2, 1])
        
        with left_col:
            # Home button
            if st.button("🏠 Home"):
                st.session_state.current_page = "home"
                st.rerun()
        
        with center_col:
            # Title
            st.title("Grief Support System")
        
        with right_col:
            # Profile and mood display
            if st.session_state.profile_id:
                display_user_section()

def display_user_section():
    """Display user information and current mood"""
    # Get the most recent guide for mood display
    if st.session_state.guide_history:
        latest_guide = max(
            st.session_state.guide_history,
            key=lambda x: datetime.fromisoformat(x['created_at'])
        )
        mood = latest_guide['detected_mood']
        emoji = latest_guide['mood_emoji']
        
        with st.container():
            st.write(f"{emoji} {mood.capitalize()}")
            
            # Profile button
            if st.button("👤 Profile"):
                st.session_state.current_page = "profile"
                st.rerun()
            
            # History button
            if st.button("📚 History"):
                st.session_state.current_page = "history"
                st.rerun()
    else:
        # Just show profile button if no guides yet
        if st.button("👤 Profile"):
            st.session_state.current_page = "profile"
            st.rerun()

def apply_theme():
    """Apply custom theme to the navigation bar"""
    st.markdown("""
        <style>
        .stButton button {
            width: 100%;
            border-radius: 20px;
            border: 1px solid #4CAF50;
            background-color: white;
            color: #4CAF50;
            padding: 10px 20px;
            transition: all 0.3s;
        }
        
        .stButton button:hover {
            background-color: #4CAF50;
            color: white;
        }
        
        h1 {
            color: #2E7D32;
            text-align: center;
            font-family: 'Helvetica Neue', sans-serif;
        }
        
        .user-section {
            text-align: right;
            padding: 10px;
            border-radius: 10px;
            background-color: #F1F8E9;
        }
        </style>
    """, unsafe_allow_html=True) 