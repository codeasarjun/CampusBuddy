import json
import nltk
from nltk.chat.util import Chat, reflections

# Load college information from JSON file
with open('core\college_info.json', 'r') as f:
    college_info = json.load(f)

# Define patterns and responses for the chatbot
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'college', [college_info["name"]]),
    (r'college name', [college_info["name"]]),
    (r'campus', [college_info["location"]]),
    (r'campus location', [college_info["location"]]),
    (r'website', [college_info["website"]]),
    (r'contact', [f'You can contact us at {college_info["contact"]["phone"]} or {college_info["contact"]["email"]}']),
    (r'fee', [college_info["fees"]["tuition"], college_info["fees"]["accommodation"]]),
    (r'placement', [college_info["placement"]["services"], "Our top recruiters include: " + ", ".join(college_info["placement"]["top_recruiters"])]),
    (r'program', [f'We offer the following programs: {", ".join([program["name"] for program in college_info["programs"]])}']),
    (r'facilities', [f'Our facilities include: {", ".join(college_info["facilities"])}']),
    (r'quit', ['Bye! Take care.']),
]

# Create a chatbot using NLTK's Chat class
chatbot = Chat(patterns, reflections)
