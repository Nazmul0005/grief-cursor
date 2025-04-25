import streamlit as st
from typing import Dict, List

class DailyActivity:
    def __init__(self, time_period: str, activity: str, description: str):
        self.time_period = time_period
        self.activity = activity
        self.description = description

def display_weekly_routine(routine: Dict[str, List[DailyActivity]]):
    """Display the weekly routine in an organized format"""
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    # Create tabs for each day
    tabs = st.tabs(day_names)
    
    for day, tab, day_name in zip(days, tabs, day_names):
        with tab:
            display_daily_routine(routine[day], day_name)

def display_daily_routine(activities: List[DailyActivity], day_name: str):
    """Display activities for a single day"""
    if not activities:
        st.info(f"No specific activities scheduled for {day_name}. Take time for self-care.")
        return
    
    for activity in activities:
        with st.expander(f"📅 {activity.time_period}"):
            col1, col2 = st.columns([1, 3])
            
            with col1:
                st.markdown(
                    f"""
                    <div class="activity-time">
                        <div class="time-label">{activity.time_period}</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            
            with col2:
                st.markdown(
                    f"""
                    <div class="activity-content">
                        <div class="activity-title">{activity.activity}</div>
                        <div class="activity-description">{activity.description}</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

def apply_routine_styles():
    """Apply custom CSS styles for the routine display"""
    st.markdown(
        """
        <style>
        .activity-time {
            background-color: #E3F2FD;
            padding: 10px;
            border-radius: 10px;
            text-align: center;
        }
        
        .time-label {
            color: #1976D2;
            font-weight: bold;
            font-size: 0.9em;
        }
        
        .activity-content {
            padding: 10px;
            background-color: #FFFFFF;
            border-radius: 10px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }
        
        .activity-title {
            color: #2E7D32;
            font-weight: bold;
            font-size: 1.1em;
            margin-bottom: 5px;
        }
        
        .activity-description {
            color: #616161;
            font-size: 0.95em;
            line-height: 1.4;
        }
        
        /* Style for the expander */
        .streamlit-expanderHeader {
            background-color: #F5F5F5;
            border-radius: 10px;
        }
        
        .streamlit-expanderHeader:hover {
            background-color: #EEEEEE;
        }
        
        /* Custom styles for tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 8px;
        }
        
        .stTabs [data-baseweb="tab"] {
            background-color: #FFFFFF;
            border-radius: 4px;
            padding: 8px 16px;
            box-shadow: 0 1px 2px rgba(0,0,0,0.1);
        }
        
        .stTabs [aria-selected="true"] {
            background-color: #4CAF50;
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def create_sample_routine() -> Dict[str, List[DailyActivity]]:
    """Create a sample routine for testing"""
    return {
        "monday": [
            DailyActivity(
                "Morning (9 AM-12 PM)",
                "Gentle Exercise",
                "Start with 10 minutes of stretching followed by a short walk"
            ),
            DailyActivity(
                "Afternoon (2 PM-4 PM)",
                "Journaling",
                "Write about your feelings and memories"
            )
        ],
        "tuesday": [
            DailyActivity(
                "Morning (10 AM)",
                "Support Group",
                "Attend virtual grief support group meeting"
            )
        ],
        # Add more days as needed
    } 