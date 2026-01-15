"""because of the version of some files in the 'reuiqrements txt' 
there is a necessity to install some up-to-date versinos of those requireemtns and libraries
see more details in the error message when running 'pip3 install -r requirement.txt' in the terminal """

import os 
from dotenv import load_dotenv



load_dotenv()

todoist_api_key = os.getenv('TODOIST_API_KEY')
gemini_api_key = os.getenv('GEMINI_API_KEY')

print(todoist_api_key)
print(gemini_api_key)