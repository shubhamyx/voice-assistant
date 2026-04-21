# Voice Assistant

AI-powered voice assistant that transcribes speech and responds intelligently.

## What it does
- Records your voice via microphone
- Transcribes speech to text using OpenAI Whisper
- Sends transcription to Groq LLM for a response
- Displays both transcription and AI response

## Tech Stack
- **Speech-to-Text**: OpenAI Whisper (base model)
- **LLM**: Groq API (llama-3.3-70b-versatile)
- **Framework**: LangChain
- **UI**: Gradio

## Setup

1. Clone the repo
2. Create virtual environment and activate it
3. Install dependencies

    pip install openai-whisper gradio langchain-groq python-dotenv

4. Install ffmpeg and add to PATH
5. Create `.env` file

    GROQ_API_KEY=your_key_here

6. Run

    python app.py

7. Open `http://127.0.0.1:7860`

## Built by
Shubham Yadav — building AI projects in public