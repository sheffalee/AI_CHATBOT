# Import the required libraries
import openai
import streamlit as st

# Set the OpenAI API key
openai.api_key = "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"

# Initialize session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Define a function to generate a response from OpenAI's GPT-3 model
def generate_response(prompt):
    # Create a completion using the GPT-3 engine
    completions = openai.Completion.create(
        engine="text-davinci-003",  # Choose the GPT-3 engine
        prompt=prompt,              # The input prompt for the model
        max_tokens=1024,            # Maximum number of tokens in the response
        n=1,                        # Generate only one response
        stop=None,                  # No stopping criteria
        temperature=0.5,            # Control the randomness of the response
    )

    # Get the generated text from the response
    message = completions.choices[0].text
    return message

# Set up the Streamlit app title and styling
st.title("ChatBot : Streamlit + openAI")
st.markdown(
    """
    <style>
        /* Add custom CSS styling here */
        body {
            background-color: #1a1a1a;
            color: #ffffff;
            font-family: Arial, sans-serif;
        }
        .chat-container {
            display: flex;
            flex-direction: column;  /* Display newer messages above */
            margin: 20px 0;
        }
        .user-message {
            align-self: flex-start;
            background-color: #008CBA;
            padding: 10px;
            border-radius: 10px;
            max-width: 60%;
            margin-top: 5px;
        }
        .chatbot-message {
            align-self: flex-end;
            background-color: #4CAF50;
            padding: 10px;
            border-radius: 10px;
            max-width: 60%;
            margin-top: 5px;
        }
    </style>
    """,
    unsafe_allow_html=True
)
