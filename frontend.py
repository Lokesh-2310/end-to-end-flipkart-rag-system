import streamlit as st
import requests

# Initialize session state to store chat messages
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("Flipkart Recommendation Chatbot")


# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle user input
if user_input := st.chat_input("Type your message..."):
    # Display user message
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    url = "http://127.0.0.1:8000/fetch"
    data = {"user_input": user_input}

    response = requests.post(url, json=data)
    if response.status_code == 200:
        result = response.json()
        bot_response = result["messages"]
    else:
        bot_response = "Some error occured"
        
    st.chat_message("assistant").markdown(bot_response)
    st.session_state.messages.append({"role": "assistant", "content": bot_response})

