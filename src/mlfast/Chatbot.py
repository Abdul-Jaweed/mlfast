import openai
from gradio import gradio as gr


import warnings
warnings.filterwarnings("ignore") 


def Chatbot(api_key, role, deploy=False):
    # Set up the OpenAI API client
    openai.api_key = api_key

    # Initialize the conversation with the system message based on the role
    messages = [{"role": "system", "content": f"You are {role}. How can I assist you today?"}]

    def generate_response(input_text):
        # Get user input
        message = input_text

        # Add user message to the conversation
        messages.append({"role": "user", "content": message})

        # Check if user wants to quit
        if message.lower() == "bye":
            return "Goodbye!"

        # Generate a response from the chatbot
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        # Get the assistant's reply from the response
        reply = response.choices[0].message.content

        # Add assistant's reply to the conversation
        messages.append({"role": "assistant", "content": reply})

        return reply

    title = f"{role}"
    inputs = gr.inputs.Textbox(label="User Input")
    outputs = gr.outputs.Textbox(label="Assistant Reply")

    interface = gr.Interface(fn=generate_response, inputs=inputs, outputs=outputs, title=title)
    
    if deploy==True:
      interface.launch(share=True)
    else:
      interface.close()