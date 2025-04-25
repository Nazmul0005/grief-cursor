import streamlit as st
from datetime import datetime

def display_history():
    """Display the user's guide history"""
    st.write("# Your Journey")
    
    if not st.session_state.guide_history:
        st.info("You haven't generated any guides yet. Complete an assessment to get started.")
        if st.button("Start Assessment"):
            st.session_state.current_page = "assessment"
            st.rerun()
        return
    
    # Sort guides by date (newest first)
    sorted_guides = sorted(
        st.session_state.guide_history,
        key=lambda x: datetime.fromisoformat(x['created_at']),
        reverse=True
    )
    
    # Group guides by month
    current_month = None
    for guide in sorted_guides:
        guide_date = datetime.fromisoformat(guide['created_at'])
        month_year = guide_date.strftime("%B %Y")
        
        if month_year != current_month:
            st.write(f"## {month_year}")
            current_month = month_year
        
        with st.container():
            col1, col2 = st.columns([1, 4])
            
            with col1:
                st.write(f"### {guide['mood_emoji']}")
                st.write(guide_date.strftime("%d %b"))
            
            with col2:
                with st.expander("View Guide Summary"):
                    st.write(guide['overview'][:200] + "...")
                    st.write("---")
                    st.write("### Key Elements:")
                    st.write("- " + "\n- ".join(guide['coping_strategies'][:3]))
                    
                    if st.button("Open Full Guide", key=guide['id']):
                        st.session_state.current_guide = guide
                        st.session_state.current_page = "guide"
                        st.rerun()
    
    # Statistics section
    st.write("## Your Progress")
    
    # Calculate mood trends
    mood_counts = {}
    for guide in sorted_guides:
        mood = guide['detected_mood']
        mood_counts[mood] = mood_counts.get(mood, 0) + 1
    
    # Display mood distribution
    st.write("### Emotional Journey")
    cols = st.columns(len(mood_counts))
    for col, (mood, count) in zip(cols, mood_counts.items()):
        with col:
            st.metric(
                f"{mood.capitalize()} {guide['mood_emoji']}",
                f"{count} times"
            )
    
    # Most used coping strategies
    strategy_counts = {}
    for guide in sorted_guides:
        for strategy in guide['coping_strategies']:
            strategy_counts[strategy] = strategy_counts.get(strategy, 0) + 1
    
    # Sort strategies by frequency
    top_strategies = sorted(
        strategy_counts.items(),
        key=lambda x: x[1],
        reverse=True
    )[:3]
    
    st.write("### Most Used Coping Strategies")
    for strategy, count in top_strategies:
        st.write(f"- {strategy}: Used in {count} guides")
    
    # Navigation
    if st.button("Start New Assessment"):
        st.session_state.assessment_step = 1
        st.session_state.current_page = "assessment"
        st.rerun() 