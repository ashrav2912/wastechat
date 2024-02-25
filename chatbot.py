import streamlit as st
import cohere

st.set_page_config(layout='wide',page_title='Garbage image classification')
def chatbot(model_answer):
    st.title("Chatbot")
    co_api_key = st.secrets["CO_API_KEY"]  # Set Cohere API key
    co = cohere.Client(api_key=co_api_key)

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    # Display chat messages from history on app rerun
    for message in st.session_state["messages"]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("What do you want to know about " + model_answer+ "?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)

        prompt_memory = ""
        for message in st.session_state["messages"]:
            prompt_memory += message["role"] + ": " + message["content"] + "\n"
        # Display assistant response in chat message container
        print(prompt_memory)
        with st.chat_message("assistant"):
            answer = co.chat(
                prompt_memory, 
                model='command',
            )
            response = answer.text
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
 

if __name__=="__main__":
    chatbot("cardboard")