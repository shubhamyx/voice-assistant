import gradio as gr
import whisper
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

whisper_model = whisper.load_model("base")

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.3-70b-versatile"
)

prompt = ChatPromptTemplate.from_template("""
You are a helpful voice assistant. Answer concisely and clearly.
User said: {text}
""")

chain = prompt | llm | StrOutputParser()

def transcribe_and_respond(audio):
    if audio is None:
        return "No audio detected.", ""
    
    result = whisper_model.transcribe(audio)
    transcription = result["text"]
    
    response = chain.invoke({"text": transcription})
    
    return transcription, response

with gr.Blocks(title="Voice Assistant") as app:
    gr.Markdown("# Voice Assistant")
    gr.Markdown("Click the microphone, speak, and get an AI response.")
    
    audio_input = gr.Audio(type="filepath", label="Speak here")
    submit_btn = gr.Button("Get Response", variant="primary")
    
    with gr.Row():
        transcription_out = gr.Textbox(label="What you said", interactive=False)
        response_out = gr.Textbox(label="AI Response", interactive=False)
    
    submit_btn.click(
        fn=transcribe_and_respond,
        inputs=[audio_input],
        outputs=[transcription_out, response_out]
    )

app.launch()