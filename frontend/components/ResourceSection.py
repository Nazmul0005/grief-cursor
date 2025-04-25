import streamlit as st
from typing import List, Dict

class Resource:
    def __init__(self, title: str, description: str, category: str, url: str = None, contact: str = None):
        self.title = title
        self.description = description
        self.category = category
        self.url = url
        self.contact = contact

def display_resources(resources: List[Resource]):
    """Display resources organized by category"""
    st.write("## Support Resources")
    st.write("Here are some resources that may help you on your journey.")
    
    # Group resources by category
    categorized_resources: Dict[str, List[Resource]] = {}
    for resource in resources:
        if resource.category not in categorized_resources:
            categorized_resources[resource.category] = []
        categorized_resources[resource.category].append(resource)
    
    # Create tabs for each category
    categories = list(categorized_resources.keys())
    if categories:
        tabs = st.tabs(categories)
        
        for category, tab in zip(categories, tabs):
            with tab:
                display_category_resources(categorized_resources[category])

def display_category_resources(resources: List[Resource]):
    """Display resources for a specific category"""
    for resource in resources:
        with st.expander(resource.title):
            st.write(resource.description)
            
            if resource.url:
                st.markdown(f"[Learn More]({resource.url})")
            
            if resource.contact:
                st.markdown(
                    f"""
                    <div class="contact-info">
                        📞 Contact: {resource.contact}
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            
            # Add to favorites button
            if st.button("⭐ Save to Favorites", key=f"fav_{resource.title}"):
                add_to_favorites(resource)

def add_to_favorites(resource: Resource):
    """Add a resource to the user's favorites"""
    if "favorite_resources" not in st.session_state:
        st.session_state.favorite_resources = []
    
    # Check if already in favorites
    if resource.title not in [r.title for r in st.session_state.favorite_resources]:
        st.session_state.favorite_resources.append(resource)
        st.success(f"Added '{resource.title}' to your favorites!")
    else:
        st.info("This resource is already in your favorites.")

def display_favorite_resources():
    """Display the user's favorite resources"""
    if "favorite_resources" in st.session_state and st.session_state.favorite_resources:
        st.write("### Your Saved Resources")
        
        for resource in st.session_state.favorite_resources:
            with st.expander(f"⭐ {resource.title}"):
                st.write(resource.description)
                
                if resource.url:
                    st.markdown(f"[Learn More]({resource.url})")
                
                if resource.contact:
                    st.markdown(
                        f"""
                        <div class="contact-info">
                            📞 Contact: {resource.contact}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                
                if st.button("Remove from Favorites", key=f"remove_{resource.title}"):
                    st.session_state.favorite_resources.remove(resource)
                    st.rerun()

def apply_resource_styles():
    """Apply custom CSS styles for resource display"""
    st.markdown(
        """
        <style>
        /* Resource card styles */
        .resource-card {
            background-color: #FFFFFF;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            margin-bottom: 15px;
        }
        
        .resource-title {
            color: #2E7D32;
            font-size: 1.2em;
            font-weight: bold;
            margin-bottom: 10px;
        }
        
        .resource-description {
            color: #424242;
            font-size: 0.95em;
            line-height: 1.5;
            margin-bottom: 15px;
        }
        
        .contact-info {
            background-color: #F5F5F5;
            padding: 10px;
            border-radius: 5px;
            color: #616161;
            font-size: 0.9em;
            margin-top: 10px;
        }
        
        /* Tab styling */
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
        
        /* Favorite button styling */
        .stButton button {
            border-color: #FFD700;
            color: #B8860B;
        }
        
        .stButton button:hover {
            background-color: #FFD700;
            color: #000000;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def create_sample_resources() -> List[Resource]:
    """Create sample resources for testing"""
    return [
        Resource(
            "Local Grief Support Group",
            "Weekly meetings for those experiencing loss. Share your journey with others who understand.",
            "Support Groups",
            contact="555-0123"
        ),
        Resource(
            "Online Grief Counseling",
            "Professional counseling services available 24/7 through secure video chat.",
            "Professional Support",
            url="https://example.com/counseling"
        ),
        Resource(
            "Meditation for Grief App",
            "Guided meditations specifically designed for processing loss and grief.",
            "Self-Care Activities",
            url="https://example.com/meditation-app"
        ),
        Resource(
            "Crisis Hotline",
            "24/7 support line for immediate emotional support.",
            "Crisis Support",
            contact="1-800-555-0000"
        ),
        Resource(
            "Grief Journal Prompts",
            "Daily writing prompts to help process your emotions and memories.",
            "Self-Care Activities",
            url="https://example.com/journal-prompts"
        )
    ] 