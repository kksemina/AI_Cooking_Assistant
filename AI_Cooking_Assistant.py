import gradio as gr
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key= key) 


messages = [{"role": "system", "content": "You are an expern world wide chef and are here to assist with creative and healthy meal options"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply


description = """
    <h2>Welcome to the Cooking Assistant App!</h2>
    <p>This app helps you with cooking recipes and tips.</p>
    """
    
    
theme = gr.themes.Soft(
    primary_hue="lime",
    secondary_hue="emerald",
    neutral_hue="zinc",
).set(
    background_fill_primary='*neutral_300',
    link_text_color='*border_color_accent',
    link_text_color_dark='*secondary_800'
)


# Define the input component with a custom label
input_component = gr.Textbox(label="Ask the Cooking Assistant what to make for dinner tonight....")

# Define the output component with a custom label
output_component = gr.Text(label="Bonjour there! I am your personal AI Cooking Assistant!")

app = gr.Interface(
    fn=CustomChatGPT,
    inputs= input_component,  # Use the custom input component
    outputs= output_component,  # Use the custom output component
    title="Cooking Assistant",
    description=description,
    theme= theme 
)

app.launch(share=True)