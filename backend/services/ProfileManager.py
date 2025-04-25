import json
import os
from typing import Optional
from models.AssessmentModel import AssessmentModel

class ProfileManager:
    def __init__(self, data_dir: str = "data"):
        self.data_dir = data_dir
        self.profiles_file = os.path.join(data_dir, "profiles.json")
        self._ensure_data_directory()
        self._ensure_profiles_file()

    def _ensure_data_directory(self):
        """Ensure the data directory exists."""
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)

    def _ensure_profiles_file(self):
        """Ensure the profiles file exists with an empty list."""
        if not os.path.exists(self.profiles_file):
            with open(self.profiles_file, 'w') as f:
                json.dump([], f)

    def save_profile(self, profile_data: AssessmentModel) -> bool:
        """
        Save a new profile to the profiles file.
        
        Args:
            profile_data: The profile data to save
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Read existing profiles
            with open(self.profiles_file, 'r') as f:
                profiles = json.load(f)
            
            # Convert profile data to dict and add to profiles
            profile_dict = profile_data.model_dump()
            profiles.append(profile_dict)
            
            # Write updated profiles back to file
            with open(self.profiles_file, 'w') as f:
                json.dump(profiles, f, indent=2)
            
            return True
        except Exception as e:
            print(f"Error saving profile: {str(e)}")
            return False

    def get_profiles(self) -> list:
        """
        Get all saved profiles.
        
        Returns:
            list: List of all saved profiles
        """
        try:
            with open(self.profiles_file, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error reading profiles: {str(e)}")
            return [] 