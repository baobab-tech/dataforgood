from google import genai
from google.genai.types import HttpOptions
import os
from dotenv import load_dotenv

load_dotenv()

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'vertex_service_account.json'

client = genai.Client(http_options=HttpOptions(api_version="v1"), vertexai=True, project=os.getenv('GOOGLE_VERTEX_PROJECT_ID'), location=os.getenv('GOOGLE_VERTEX_LOCATION'))
response = client.models.generate_content(
    model="gemini-1.5-flash-002",
    contents="How does AI work?",
    
)
print(response.text)
