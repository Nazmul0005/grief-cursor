# Grief Support System

A compassionate digital platform that provides personalized grief support through AI-generated guides, reflective exercises, and resource recommendations.

## Features

- **Personalized Profile Creation**: Collect user information to provide tailored support
- **Grief Assessment**: Comprehensive questionnaire to understand the user's grief journey
- **AI-Generated Support Guides**: Custom guides with:
  - Weekly routines
  - Reflective questions
  - Physical activity recommendations
  - Meal planning suggestions
  - Evening rituals
  - Coping strategies
- **Resource Recommendations**: Local and online support resources
- **Mood Tracking**: Emotional state analysis and tracking
- **Guide History**: Access to previously generated guides

## Setup

1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   Create a `.env` file in the root directory with:
   ```
   GROQ_API_KEY=your_api_key_here
   ```

4. Start the backend server:
   ```bash
   cd backend
   uvicorn main:app --reload
   ```

5. Start the Streamlit frontend:
   ```bash
   cd frontend
   streamlit run app.py
   ```

## Project Structure

```
grief_support_system/
├── frontend/              # Streamlit web application
├── backend/              # FastAPI backend server
└── shared/              # Shared constants and utilities
```

## API Documentation

Once the backend server is running, visit:
- API documentation: http://localhost:8000/docs
- Alternative documentation: http://localhost:8000/redoc

## Frontend Pages

1. **Home Page**: Landing page with start assessment button
2. **Profile Page**: Collects user information
3. **Assessment Page**: Grief assessment questionnaire
4. **Guide Display Page**: Shows the generated grief guide
5. **History Page**: Displays saved guides

## Development

- Backend API: FastAPI with Python 3.8+
- Frontend: Streamlit
- AI Integration: Groq API (Mixtral model)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 