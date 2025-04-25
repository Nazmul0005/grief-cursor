import streamlit as st
from datetime import datetime

def display_guide():
    """Display the generated grief guide"""
    if "current_guide" not in st.session_state:
        st.error("No guide to display. Please complete the assessment first.")
        return
    
    guide = st.session_state.current_guide
    
    # Header with mood
    st.write(f"# Your Personal Grief Guide {guide['mood_emoji']}")
    st.write(f"*Generated on {datetime.fromisoformat(guide['created_at']).strftime('%B %d, %Y')}*")
    
    # Overview section
    st.write("## Overview")
    st.write(guide['overview'])
    
    # Weekly routine
    st.write("## Your Weekly Routine")
    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    
    tab_titles = [day.capitalize() for day in days]
    tabs = st.tabs(tab_titles)
    
    for day, tab in zip(days, tabs):
        with tab:
            activities = guide['weekly_routine'][day]
            if activities:
                for activity in activities:
                    with st.expander(f"📅 {activity['time_period']}"):
                        st.write(f"**{activity['activity']}**")
                        st.write(activity['description'])
            else:
                st.info("No specific activities scheduled for this day. Take time for self-care.")
    
    # Reflective questions
    st.write("## Reflective Questions")
    st.write("Take time to consider these questions when you feel ready.")
    
    for i, question in enumerate(guide['reflective_questions'], 1):
        with st.expander(f"Question {i}: {question['question']}"):
            st.write(f"*{question['context']}*")
            st.write("\nSuggested prompts to consider:")
            for prompt in question['suggested_prompts']:
                st.write(f"- {prompt}")
    
    # Daily recommendations
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.write("### Physical Activity")
        with st.expander("View Recommendation"):
            st.write(guide['physical_activity'])
    
    with col2:
        st.write("### Meal Planning")
        with st.expander("View Recommendation"):
            st.write(guide['meal_plan'])
    
    with col3:
        st.write("### Evening Ritual")
        with st.expander("View Recommendation"):
            st.write(guide['evening_ritual'])
    
    # Coping strategies
    st.write("## Recommended Coping Strategies")
    strategy_cols = st.columns(len(guide['coping_strategies']))
    for col, strategy in zip(strategy_cols, guide['coping_strategies']):
        with col:
            st.markdown(f"### 🌟\n{strategy}")
    
    # Resources
    st.write("## Support Resources")
    for resource in guide['resources']:
        with st.expander(f"{resource['title']} ({resource['category']})"):
            st.write(resource['description'])
            if resource.get('url'):
                st.write(f"[Learn More]({resource['url']})")
            if resource.get('contact'):
                st.write(f"Contact: {resource['contact']}")
    
    # Navigation buttons
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        if st.button("← Back to Home"):
            st.session_state.current_page = "home"
            st.rerun()
    with col3:
        if st.button("Start New Assessment →"):
            st.session_state.assessment_step = 1
            st.session_state.current_page = "assessment"
            st.rerun() 