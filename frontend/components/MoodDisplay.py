import streamlit as st
from typing import Dict, Tuple

def get_mood_message(mood: str) -> Tuple[str, str]:
    """Get the emoji and supportive message for a mood"""
    mood_map: Dict[str, Tuple[str, str]] = {
        "devastated": (
            "😢",
            "It's okay to feel overwhelmed. Take things one moment at a time."
        ),
        "sad": (
            "😔",
            "Your feelings are valid. Be gentle with yourself today."
        ),
        "anxious": (
            "😰",
            "Remember to breathe. This moment will pass."
        ),
        "angry": (
            "😠",
            "Your anger is a natural response to loss. Allow yourself to feel it."
        ),
        "numb": (
            "😶",
            "Not feeling is also a way of feeling. Give yourself time."
        ),
        "hopeful": (
            "🌱",
            "Hope is growing within you. Nurture it gently."
        ),
        "accepting": (
            "🙏",
            "You're finding your way through this. That takes courage."
        ),
        "grateful": (
            "💗",
            "Cherish the memories and love that remain."
        )
    }
    
    return mood_map.get(mood, ("😌", "Take each day as it comes."))

def display_mood(mood: str):
    """Display the mood emoji and supportive message"""
    emoji, message = get_mood_message(mood.lower())
    
    with st.container():
        st.markdown(
            f"""
            <div class="mood-container">
                <div class="mood-emoji">{emoji}</div>
                <div class="mood-text">{mood.capitalize()}</div>
                <div class="mood-message">{message}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

def apply_mood_styles():
    """Apply custom CSS styles for mood display"""
    st.markdown(
        """
        <style>
        .mood-container {
            padding: 20px;
            border-radius: 15px;
            background-color: #F8F9FA;
            text-align: center;
            margin: 10px 0;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        
        .mood-emoji {
            font-size: 2.5em;
            margin-bottom: 10px;
            animation: float 3s ease-in-out infinite;
        }
        
        .mood-text {
            font-size: 1.2em;
            color: #495057;
            margin-bottom: 10px;
            font-weight: bold;
        }
        
        .mood-message {
            color: #6C757D;
            font-style: italic;
            line-height: 1.4;
        }
        
        @keyframes float {
            0% {
                transform: translateY(0px);
            }
            50% {
                transform: translateY(-5px);
            }
            100% {
                transform: translateY(0px);
            }
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def display_mood_history(moods: list):
    """Display a timeline of mood changes"""
    st.write("### Your Emotional Journey")
    
    for i, mood_data in enumerate(moods):
        mood = mood_data['mood']
        date = mood_data['date']
        emoji, _ = get_mood_message(mood.lower())
        
        col1, col2 = st.columns([1, 4])
        with col1:
            st.write(f"{emoji}")
        with col2:
            st.write(f"**{mood.capitalize()}**")
            st.write(f"*{date}*")
        
        if i < len(moods) - 1:
            st.markdown("---") 