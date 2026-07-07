import os
from dotenv import load_dotenv

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")

if not NEWS_API_KEY:
    print("WARNING: NEWS_API_KEY not found. Make sure you have a .env file with NEWS_API_KEY=your_key_here")