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
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",
            prompt="\n".join([f"{m['role']}: {m['content']}" for m in messages]),
            temperature=0.7,
            max_tokens=50,
            n=1,
            stop=None
        )

        # Get the assistant's reply from the response
        reply = response.choices[0].text.strip()

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