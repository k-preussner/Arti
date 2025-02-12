import streamlit as st
from streamlit_chat import message

# Set page config
st.set_page_config(page_title="Artisan Partners - Mimic", layout="wide")

# Custom CSS for styling
st.markdown(
    """
    <style>
        /* Top navigation bar */
        .nav-bar {
            background-color: #2E3B4E;
            padding: 10px;
            color: white;
            font-size: 18px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .nav-bar a {
            color: white;
            text-decoration: none;
            margin: 0 15px;
        }

        .nav-bar a:hover {
            text-decoration: underline;
        }

        /* Chatbot styling */
        .chat-bot-container {
            position: fixed;
            bottom: 20px;
            left: 20px;
            width: 300px;
            background-color: white;
            border: 1px solid #ddd;
            border-radius: 10px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }

        .chat-bot-header {
            background-color: #2E3B4E;
            color: white;
            padding: 10px;
            text-align: center;
            border-top-left-radius: 10px;
            border-top-right-radius: 10px;
        }

        .chat-bot-body {
            padding: 10px;
            max-height: 300px;
            overflow-y: auto;
        }

        .chat-bot-input {
            border-top: 1px solid #ddd;
            padding: 10px;
        }

    </style>
    """,
    unsafe_allow_html=True,
)

# Top Navigation Bar
st.markdown(
    """
    <div class="nav-bar">
        <div>Artisan Partners</div>
        <div>
            <a href="#">Strategies</a>
            <a href="#">Insights</a>
            <a href="#">About</a>
            <a href="#">Contact</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Main Content Area
st.title("Welcome to Artisan Partners")
st.write(
    "Discover our strategies, insights, and commitment to delivering exceptional outcomes for our clients."
)

# Placeholder for chatbot
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Chatbot container
with st.container():
    st.markdown(
        """
        <div class="chat-bot-container">
            <div class="chat-bot-header">Chat with Us</div>
            <div class="chat-bot-body">
        """,
        unsafe_allow_html=True,
    )

    # Display chat messages
    for message_data in st.session_state.messages:
        if message_data["is_user"]:
            message(message_data["content"], is_user=True, key=f"user-{message_data['key']}")
        else:
            message(message_data["content"], is_user=False, key=f"bot-{message_data['key']}")

    st.markdown(
        """
            </div>
            <div class="chat-bot-input">
                <form action="javascript:void(0);">
                    <input type="text" id="user_input" style="width: 100%; padding: 5px;" placeholder="Type your message here...">
                </form>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Chatbot interaction logic
user_input = st.text_input("Chatbot Input", "", key="chatbot")
if user_input:
    st.session_state.messages.append({"content": user_input, "is_user": True, "key": len(st.session_state.messages)})
    # Example response
    bot_response = "Thank you for your question! How can I assist you further?"
    st.session_state.messages.append({"content": bot_response, "is_user": False, "key": len(st.session_state.messages)})
