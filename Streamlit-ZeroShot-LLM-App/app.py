import prompts, llm_connection
import streamlit as st

# Function to simulate generating a response (this can be replaced with real logic)
def get_response(query):
    prompt = prompts.DreamPrompt.prompt1 + f"\nDream:\n{query}\nAnalysis:"
    return llm_connection.CohereAPI.invoke(prompt)

# Function to display the homepage with the query input and button
def show_home_page():
    st.title("Welcome to the Dreamify")

    # User input for query
    query = st.text_input("Describe the dream you just woke up from:")
    
    # Button to trigger the query process
    if st.button("Look Up") or query:
        if query:
            # Save query to session state
            st.session_state.query = query
            st.session_state.response = get_response(query)
            show_response_page()  # Transition to the response page

# Function to display the response page with question and response
def show_response_page():
    if 'query' in st.session_state and 'response' in st.session_state:
        query = st.session_state.query
        response = st.session_state.response
        
        # Display question and response in a chat-like format
        col1, col2 = st.columns([1, 3])  # Left for question, right for response
        
        with col1:
            st.markdown(f"**Dream:** {query}")
        
        with col2:
            st.markdown(f"**Analysis:** {response}")
        
        # No retry button; the user simply sees the response and cannot go back.

# Main app execution
if 'query' not in st.session_state or 'response' not in st.session_state:
    show_home_page()  # Show the homepage if no query is stored in session state
else:
    show_response_page()  # Show the response page if query and response are stored

# Optional: Custom CSS for styling (responsive design)
st.markdown("""
    <style>
        /* Center align the entire page */
        .css-1d391kg {
            display: flex;
            justify-content: center;
            flex-direction: column;
            align-items: center;
        }

        /* Chat interface: Style for question and response */
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            font-size: 14px;
            border-radius: 5px;
            border: none;
            cursor: pointer;
        }

        .stButton>button:hover {
            background-color: #45a049;
        }

        /* Responsive: On smaller screens, adjust input width */
        @media (max-width: 600px) {
            .css-1d391kg {
                width: 100%;
                align-items: center;
            }

            .stTextInput>div>input {
                width: 80%;
            }

            .stButton>button {
                width: 80%;
                margin-top: 10px;
            }
        }
    </style>
""", unsafe_allow_html=True)
