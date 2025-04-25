import streamlit as st
from typing import List, Dict

class ReflectiveQuestion:
    def __init__(self, question: str, context: str, suggested_prompts: List[str]):
        self.question = question
        self.context = context
        self.suggested_prompts = suggested_prompts

def display_reflective_questions(questions: List[ReflectiveQuestion]):
    """Display reflective questions in an interactive format"""
    st.write("## Reflective Questions")
    st.write("Take time to consider these questions when you feel ready. Click on each card to explore further.")
    
    # Initialize session state for responses if not exists
    if "question_responses" not in st.session_state:
        st.session_state.question_responses = {}
    
    # Create a grid layout for question cards
    cols = st.columns(min(len(questions), 3))
    
    for i, (question, col) in enumerate(zip(questions, cols * (len(questions) // 3 + 1))):
        with col:
            display_question_card(question, i)

def display_question_card(question: ReflectiveQuestion, index: int):
    """Display a single question card"""
    card_id = f"question_{index}"
    
    with st.container():
        st.markdown(
            f"""
            <div class="question-card">
                <div class="question-number">Question {index + 1}</div>
                <div class="question-text">{question.question}</div>
                <div class="question-context">{question.context}</div>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        if st.button("Reflect", key=card_id):
            show_reflection_dialog(question, card_id)

def show_reflection_dialog(question: ReflectiveQuestion, card_id: str):
    """Show a dialog for reflecting on the question"""
    st.markdown("---")
    st.write(f"### {question.question}")
    st.write(f"*{question.context}*")
    
    st.write("\n**Prompts to consider:**")
    for prompt in question.suggested_prompts:
        st.write(f"- {prompt}")
    
    # Get previous response if exists
    previous_response = st.session_state.question_responses.get(card_id, "")
    
    response = st.text_area(
        "Your thoughts:",
        value=previous_response,
        height=150,
        key=f"{card_id}_response"
    )
    
    col1, col2 = st.columns([1, 4])
    with col1:
        if st.button("Save", key=f"{card_id}_save"):
            st.session_state.question_responses[card_id] = response
            st.success("Response saved!")
    
    with col2:
        if response and st.button("Clear", key=f"{card_id}_clear"):
            st.session_state.question_responses[card_id] = ""
            st.rerun()

def apply_question_styles():
    """Apply custom CSS styles for question cards"""
    st.markdown(
        """
        <style>
        .question-card {
            background-color: #FFFFFF;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            margin-bottom: 20px;
            transition: transform 0.2s;
            cursor: pointer;
        }
        
        .question-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 4px 10px rgba(0,0,0,0.15);
        }
        
        .question-number {
            color: #4CAF50;
            font-weight: bold;
            font-size: 0.9em;
            margin-bottom: 10px;
        }
        
        .question-text {
            color: #212121;
            font-size: 1.1em;
            font-weight: bold;
            margin-bottom: 10px;
            line-height: 1.4;
        }
        
        .question-context {
            color: #757575;
            font-size: 0.9em;
            font-style: italic;
            line-height: 1.4;
        }
        
        /* Style for the reflection dialog */
        .reflection-dialog {
            background-color: #F5F5F5;
            padding: 20px;
            border-radius: 10px;
            margin-top: 20px;
        }
        
        /* Style for prompts */
        .prompt-list {
            margin: 15px 0;
            padding-left: 20px;
        }
        
        .prompt-item {
            color: #424242;
            margin: 5px 0;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def create_sample_questions() -> List[ReflectiveQuestion]:
    """Create sample questions for testing"""
    return [
        ReflectiveQuestion(
            "What memory brings you the most comfort?",
            "Reflecting on positive memories can help in the healing process",
            [
                "Think about a time when you shared laughter",
                "Remember a moment that made you feel loved",
                "Consider a lesson they taught you"
            ]
        ),
        ReflectiveQuestion(
            "How has this loss changed your perspective?",
            "Understanding our growth through grief",
            [
                "What matters more to you now?",
                "What have you learned about yourself?",
                "How do you view relationships differently?"
            ]
        ),
        ReflectiveQuestion(
            "What would you want them to know?",
            "Express your thoughts to your loved one",
            [
                "What would you like to tell them?",
                "What do you wish you had said?",
                "What are you proud to share with them?"
            ]
        )
    ] 