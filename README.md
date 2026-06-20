# AI Interview Chatbot

## Overview

The AI Interview Chatbot is a Streamlit-based web application that simulates real interview scenarios. It conducts HR and technical interviews by generating dynamic questions using an AI model and evaluates user responses with structured scoring and feedback.

The system is designed to help users practice interviews, improve communication skills, and receive AI-powered performance evaluation.

Live Demo:
https://ai-interview-chatbot-aryasmita1.streamlit.app/


## Features

- AI-generated interview questions
- HR and Technical interview modes
- Role-based interview flow (AI Engineer, Data Scientist, Software Engineer, etc.)
- Real-time question and answer interaction
- Automatic evaluation after interview completion
- Scoring based on:
  - Technical skills
  - Communication skills
  - Problem-solving ability
  - Overall performance
- Structured feedback for improvement


## Tech Stack

- Python
- Streamlit
- OpenAI / OpenRouter API
- python-dotenv


## Project Structure

ai-interview-chatbot/
│── app.py
│── requirements.txt
│── chatbot/
│   │── __init__.py
│   │── prompts.py
│   │── interviewer.py
│   │── evaluator.py



## Installation and Setup

### 1. Clone the repository

git clone https://github.com/aryasmita1/ai-interview-chatbot.git
cd ai-interview-chatbot



### 2. Create virtual environment

python -m venv venv

Activate environment:

Windows:
venv\Scripts\activate


### 3. Install dependencies

pip install -r requirements.txt


### 4. Add API Key

Create a .env file in the root directory:

OPENROUTER_API_KEY=your_api_key_here


### 5. Run the application

streamlit run app.py


## Environment Variables

OPENROUTER_API_KEY: API key for OpenRouter/OpenAI access


## How It Works

1. User selects role and interview type
2. AI generates interview questions dynamically
3. User submits answers
4. AI continues generating next questions
5. After 5 questions, system evaluates performance
6. Final report is generated with scores and feedback

## Future Improvements

- Speech-based interview mode
- PDF report download
- Advanced analytics dashboard
- Company-specific interview simulation
- Improved UI with chat-style interface



## Author

Aryasmita Panda



## License

This project is for educational and personal use.
